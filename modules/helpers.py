from .const import DATA

from settings import MAX_GWEI, RETRY
import time
from loguru import logger
from web3 import Web3
import random
from tqdm import tqdm
from time import sleep

w3_eth = Web3(Web3.HTTPProvider(random.choice(DATA['ethereum']['rpc'])))


def sign_and_check_tx(chain_w3, swap_txn, account):
    i = 0
    while i <= RETRY:
        try:
            i += 1
            if 'gasPrice' not in swap_txn:
                fee = chain_w3.eth.gas_price
                swap_txn['maxFeePerGas'] = int(fee * 1.2)
                swap_txn['maxPriorityFeePerGas'] = int(fee * 1.1)

            swap_txn['nonce'] = chain_w3.eth.get_transaction_count(account.address)
            swap_txn['gas'] = int(int(swap_txn['gas']) * 1.5)
            signed_swap_txn = chain_w3.eth.account.sign_transaction(swap_txn, account.key)
            swap_txn_hash = chain_w3.eth.send_raw_transaction(signed_swap_txn.rawTransaction)
            sleep(2)
            status = chain_w3.eth.wait_for_transaction_receipt(swap_txn_hash, timeout=120).status
            if status == 1:
                return True, swap_txn_hash
            else:
                logger.error(f'[{account.address}] Transaction failed! Trying again')
                sleep(15)
        except Exception as err:
            if 'insufficient funds' in str(err):
                logger.error(f"[{account.address}] Error send: Balance not enough")
            else:
                logger.error(f'[{account.address}] error: {type(err).__name__} {err}')
            if i <= RETRY:
                logger.info(f'[{i}/{RETRY}] trying again...')
                sleep(30)
    return False, ''


def cheker_gwei():
    try:
        max_gwei = MAX_GWEI * 10 ** 9
        if w3_eth.eth.gas_price > max_gwei:
            logger.info('Газ большой, пойду спать')
            while w3_eth.eth.gas_price > max_gwei:
                time.sleep(60)
            logger.info('Газ в норме. Продолжаю работу')
    except:
        w3_eth = Web3(Web3.HTTPProvider(random.choice(DATA['ethereum']['rpc'])))
        cheker_gwei()


def get_web3(chain):
    rpc = random.choice(DATA[chain]['rpc'])
    web3 = Web3(Web3.HTTPProvider(rpc))
    return web3


def intToDecimal(qty, decimal):
    return int(qty * int("".join(["1"] + ["0"] * decimal)))


def sleeping(from_sleep, to_sleep):
    x = random.randint(from_sleep, to_sleep)
    for i in tqdm(range(x), desc='sleep ', bar_format='{desc}: {n_fmt}/{total_fmt}'):
        time.sleep(1)
