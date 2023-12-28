from loguru import logger
from web3 import Web3
from sys import stderr
import random
from eth_abi.packed import encode_packed
from web3.middleware import geth_poa_middleware
from eth_utils import to_bytes

from settings import SLEEP_FROM, SLEEP_TO, MIN_NATIV, FROM_CHAINS, COUNT_TX, COUNT_NATIV, L2PASS_REFUEL_LIST
from .const import L2PASS_CONTRACT, LAYERZERO_CHAINS_ID, L2PASS_ABI, DATA, MINT_CONTRACT, MINT_ABI
from .helpers import get_web3, intToDecimal, sleeping, cheker_gwei, sign_and_check_tx

logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white> | <level>{level: <3}</level> | <level>{message}</level>")


def estimated_fee(dst_chain_id: int, value_wei: int, address: str, contract):
    try:
        fee = contract.functions.estimateGasRefuelFee(dst_chain_id, value_wei, address, False).call()
        return fee[0]
    except Exception as error:
        logger.error(f"Ошибка при оценке комиссии: {error}")
        return 0  # Возвращаем 0 в случае ошибки


def from_chain_balance(account, mint: bool):
    FROM_CHAINS_RETURN = []

    for chain in FROM_CHAINS:
        Fail = True
        attemp = 0
        while Fail and attemp < 5:
            attemp += 1
            try:
                min_nativ = MIN_NATIV[chain] * 10 ** 18
                if mint:
                    min_nativ = int(min_nativ * 3)
                w3 = Web3(Web3.HTTPProvider(random.choice(DATA[chain]['rpc'])))
                balance = w3.eth.get_balance(account.address)
                Fail = False
                if balance > min_nativ:
                    FROM_CHAINS_RETURN.append(chain)
            except:
                logger.warning(f'{chain} проблемы с рпц, попробую другую, если она есть спустя минуту')
                time.sleep(60)
                pass

    return FROM_CHAINS_RETURN


def refuel(accounts):
    for current_tranz in range(0, COUNT_TX[1]):
        logger.info(f'Транзакция: {current_tranz + 1}/{COUNT_TX[1]}')
        for current_account, private_key in enumerate(accounts):
            all_accounts = len(accounts)
            amount_from = COUNT_NATIV[0]
            amount_to = COUNT_NATIV[1]

            web3 = get_web3('ethereum')

            account = web3.eth.account.from_key(private_key)
            FROM_CHAINS_S_BALANCE = from_chain_balance(account, mint=False)
            if len(FROM_CHAINS_S_BALANCE) > 0:
                from_chain = random.choice(FROM_CHAINS_S_BALANCE)
            else:
                logger.warning(f'[{account.address}] Нет сетей с минимальным балансом, пропускаю кошелек....')
                continue
            to_chain = random.choice(L2PASS_REFUEL_LIST[from_chain])

            if (current_tranz + 1) > random.randint(COUNT_TX[0], COUNT_TX[1]):  # проверка на кол-во
                continue

            cheker_gwei()
            current_account += 1

            global module_str

            try:
                amount = round(random.uniform(amount_from, amount_to), 8)

                web3 = get_web3(from_chain)
                account = web3.eth.account.from_key(private_key)
                web3.middleware_onion.inject(geth_poa_middleware, layer=0)
                wallet = account.address

                module_str = f'{from_chain} => {to_chain}'
                logger.info(f'[{current_account}/{all_accounts}][{wallet}] {module_str}')

                contract = web3.eth.contract(address=Web3.to_checksum_address(
                    L2PASS_CONTRACT), abi=L2PASS_ABI)

                value = intToDecimal(amount, 18)

                refuel_fee_wei = estimated_fee(LAYERZERO_CHAINS_ID[to_chain], value, wallet,
                                               contract)

                refuel_txn = contract.functions.gasRefuel(
                    LAYERZERO_CHAINS_ID[to_chain],
                    '0x0000000000000000000000000000000000000000',
                    value,
                    wallet,
                )

                params = {
                    'from': wallet,
                    'value': refuel_fee_wei,
                }

                if amount > 0:

                    if from_chain in {'kava evm', 'moonbeam', 'bsc'}:
                        params['gasPrice'] = int(web3.eth.gas_price * 1.1)

                    refuel_txn = refuel_txn.build_transaction(params)

                    success_tx, swap_txn_hash = sign_and_check_tx(web3, refuel_txn, account)
                    if success_tx:
                        logger.success(f"{DATA[from_chain]['scan']}/{swap_txn_hash.hex()}")

                else:
                    logger.error(f"{module_str} : баланс равен 0")

            except Exception as error:
                logger.error(f'{module_str} | {error}')

            sleeping(SLEEP_FROM, SLEEP_TO)
        sleeping(SLEEP_FROM, SLEEP_TO)


def mint_bridge(accounts):
    for current_tranz in range(0, COUNT_TX[1]):
        logger.info(f'Транзакция: {current_tranz + 1}/{COUNT_TX[1]}')
        for current_account, private_key in enumerate(accounts):

            web3 = get_web3('ethereum')

            account = web3.eth.account.from_key(private_key)
            FROM_CHAINS_S_BALANCE = from_chain_balance(account, mint=True)
            if len(FROM_CHAINS_S_BALANCE) > 0:
                from_chain = random.choice(FROM_CHAINS_S_BALANCE)
            else:
                logger.warning(f'[{account.address}] Нет сетей с минимальным балансом, пропускаю кошелек....')
                continue
            to_chain = random.choice(L2PASS_REFUEL_LIST[from_chain])

            if (current_tranz + 1) > random.randint(COUNT_TX[0], COUNT_TX[1]):  # проверка на кол-во
                continue

            cheker_gwei()
            current_account += 1

            global module_str

            success = mint(from_chain, to_chain, private_key, current_account, len(accounts))
            sleeping(SLEEP_FROM, SLEEP_TO)
            if success:
                bridge(from_chain, to_chain, private_key)

            sleeping(SLEEP_FROM, SLEEP_TO)


def mint(from_chain, to_chain, private_key, current_account, all_accounts):
    try:
        web3 = get_web3(from_chain)
        account = web3.eth.account.from_key(private_key)
        web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        wallet = account.address

        module_str = f'Минт и бридж {from_chain} => {to_chain}'
        logger.info(f'[{current_account}/{all_accounts}][{wallet}] {module_str}')

        contract = web3.eth.contract(address=Web3.to_checksum_address(
            MINT_CONTRACT), abi=MINT_ABI)

        mint_fee = contract.functions.mintPrice().call()
        mint_txn = contract.functions.mint(1)

        params = {
            'from': wallet,
            'value': mint_fee
        }

        if from_chain in {'kava evm', 'moonbeam', 'bsc'}:
            params['gasPrice'] = int(web3.eth.gas_price * 1.1)

        mint_txn = mint_txn.build_transaction(params)

        chain_fee = web3.eth.estimate_gas(mint_txn)

        mint_txn['value'] = mint_fee + chain_fee

        success_tx, swap_txn_hash = sign_and_check_tx(web3, mint_txn, account)
        if success_tx:
            logger.success(f"Минт tx:{DATA[from_chain]['scan']}/{swap_txn_hash.hex()}")
            return True

    except Exception as error:
        logger.error(f'{module_str} | {error}')


def bridge(from_chain, to_chain, private_key):
    try:
        web3 = get_web3(from_chain)
        account = web3.eth.account.from_key(private_key)
        web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        wallet = account.address
        contract = web3.eth.contract(address=web3.to_checksum_address(MINT_CONTRACT), abi=MINT_ABI)

        module_str = f'Бридж {from_chain} => {to_chain}'

        nft_balance = contract.functions.balanceOf(wallet).call()

        token_index = random.randint(0, nft_balance - 1)
        token_id = contract.functions.tokenOfOwnerByIndex(wallet, token_index).call()

        logger.info(f"Bridge NFT to {to_chain}")

        adapterParams = encode_packed(["uint16", "uint256"], [1, 200000])
        address_bytes = to_bytes(hexstr=wallet)

        nativeFee, _ = contract.functions.estimateSendFee(
            LAYERZERO_CHAINS_ID[to_chain],
            address_bytes,
            token_id,
            False,
            adapterParams
        ).call()
        bridge_fee = contract.functions.sendPrice().call()

        params = {
            'from': wallet,
            'value': nativeFee+bridge_fee,
        }

        bridge_txn = contract.functions.sendFrom(
            wallet,
            LAYERZERO_CHAINS_ID[to_chain],
            wallet,
            token_id,
            wallet,
            '0x0000000000000000000000000000000000000000',
            adapterParams
        )

        if from_chain in {'kava evm', 'moonbeam', 'bsc'}:
            params['gasPrice'] = int(web3.eth.gas_price * 1.1)

        bridge_txn = bridge_txn.build_transaction(params)

        trans_fee_wei = web3.eth.estimate_gas(bridge_txn)

        bridge_txn['value'] = trans_fee_wei + nativeFee

        success_tx, swap_txn_hash = sign_and_check_tx(web3, bridge_txn, account)
        if success_tx:
            logger.success(f"Бридж tx: {DATA[from_chain]['scan']}/{swap_txn_hash.hex()}")

    except Exception as error:
        logger.error(f'{module_str} | {error}')
