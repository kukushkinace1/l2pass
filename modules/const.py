import json

ERC20_ABI = '[{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"}]'

ZERO_ADDRESS = 0x0000000000000000000000000000000000000000

L2PASS_CONTRACT = '0x222228060E7Efbb1D78BB5D454581910e3922222'
L2PASS_ABI = json.load(open('./abis/refuel.json'))

MINT_CONTRACT = {
    'all':       '0x0000049F63Ef0D60aBE49fdD8BEbfa5a68822222',
    'polygon':   '0x042002711e4d7A7Fc486742a85dBf096beeb0420',
    'zksync':    '0x8582525114212C2815F13d96Ed5158553287a166',
}
MINT_ABI = json.load(open('./abis/mint.json'))

LAYERZERO_CHAINS_ID = {
    'kava evm':         177,
    'linea mainnet':    183,
    'base':             184,
    'scroll':           214,
    'celo':             125,
    'bsc':              102,
    'arbitrum nova':    175,
    'moonbeam':         126,
    'fantom':           112,
    'gnosis':           145,
    'moonriver':        167,
    'fuse':             138,
    'arbitrum':         110,
    'polygon':          109,
    'avalanche':        106,
    'polygon zkevm':    158,
    'optimism':         111,
    'mantle':           181,
    'harmony':          116,
    'opbnb':            202,
    'klaytn':           150,
    'core':             153,
    'canto':            159,
    'aurora':           211,
}


DATA = {
    'zksync':       {'rpc': ['https://zksync-era.blockpi.network/v1/rpc/public'],  'scan': 'https://explorer.zksync.io/tx',        'token': 'ETH','chain_id': 324},
    'ethereum':     {'rpc': ['https://rpc.ankr.com/eth'],       'scan': 'https://etherscan.io/tx',              'token': 'ETH', 'chain_id': 1},
    'optimism':     {'rpc': ['https://rpc.ankr.com/optimism'],  'scan': 'https://optimistic.etherscan.io/tx',   'token': 'ETH', 'chain_id': 10},
    'bsc':          {'rpc': ['https://rpc.ankr.com/bsc'],       'scan': 'https://bscscan.com/tx',               'token': 'BNB', 'chain_id': 56},
    'polygon':      {'rpc': ['https://rpc.ankr.com/polygon'],   'scan': 'https://polygonscan.com/tx',           'token': 'MATIC','chain_id': 137},
    'polygon zkevm':{'rpc': ['https://zkevm-rpc.com'],          'scan': 'https://zkevm.polygonscan.com/tx',     'token': 'ETH', 'chain_id': 1101},
    'arbitrum':     {'rpc': ['https://rpc.ankr.com/arbitrum'],  'scan': 'https://arbiscan.io/tx',               'token': 'ETH', 'chain_id': 42161},
    'avalanche':    {'rpc': ['https://rpc.ankr.com/avalanche'], 'scan': 'https://snowtrace.io/tx',              'token': 'AVAX','chain_id': 43114},
    'fantom':       {'rpc': ['https://rpc.ankr.com/fantom'],    'scan': 'https://ftmscan.com/tx',               'token': 'FTM', 'chain_id': 250},
    'arbitrum nova':{'rpc': ['https://nova.arbitrum.io/rpc'],   'scan': 'https://nova.arbiscan.io/tx',          'token': 'ETH', 'chain_id': 42170},
    'celo':         {'rpc': ['https://1rpc.io/celo'],           'scan': 'https://celoscan.io/tx',               'token': 'CELO','chain_id': 42220},
    'gnosis':       {'rpc': ['https://1rpc.io/gnosis'],         'scan': 'https://gnosisscan.io/tx',             'token': 'xDAI','chain_id': 100},
    'moonbeam':     {'rpc': ['https://moonbeam.public.blastapi.io'],  'scan': 'https://moonscan.io/tx',               'token': 'GLMR','chain_id': 1284},
    'moonriver':    {'rpc': ['https://moonriver.public.blastapi.io'],'scan': 'https://moonriver.moonscan.io/tx','token': 'MOVR','chain_id': 1285},
    'linea mainnet':{'rpc': ['https://rpc.linea.build'],        'scan': 'https://lineascan.build/tx',           'token': 'ETH', 'chain_id': 59144},
    'base':         {'rpc': ['https://mainnet.base.org'],       'scan': 'https://basescan.org/tx',              'token': 'ETH', 'chain_id': 8453},
    'mantle':       {'rpc': ['https://rpc.mantle.xyz'],         'scan': 'https://explorer.mantle.xyz/tx',       'token': 'MNT', 'chain_id': 5000},
    'fuse':         {'rpc': ['https://rpc.fuse.io'],            'scan': 'https://explorer.fuse.io/tx',          'token': 'FUSE', 'chain_id': 122},
    'scroll':       {'rpc': ['https://rpc.ankr.com/scroll'],    'scan': 'https://scrollscan.com/tx',            'token': 'ETH', 'chain_id': 534352},
    'kava evm':     {'rpc': ['https://evm.kava.io'],            'scan': 'https://kavascan.com/tx',              'token': 'KAVA', 'chain_id': 2222},
    'klaytn':       {'rpc': ['https://klaytn.blockpi.network/v1/rpc/public', 'https://rpc.ankr.com/klaytn'],            'scan': 'https://klaytnscope.com/tx',              'token': 'KAVA', 'chain_id': 2222},
}
