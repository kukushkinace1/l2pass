MAX_GWEI = 50           # гвей лимит
RETRY = 2              # попытки отправить транзакцию
SLEEP_FROM = 30          # сон от
SLEEP_TO = 50           # сон до

RANDOM_WALLETS = True # True / False


COUNT_TX = [5, 6] #от 1 до 2 транзакций

#['polygon', 'fantom', 'arbitrum nova', 'base', 'gnosis', 'optimism', 'moonbeam', 'moonriver', 'celo', 'kava evm', 'fuse', 'mantle']
FROM_CHAINS = ['polygon', 'fantom', 'arbitrum nova', 'base', 'gnosis', 'optimism', 'moonbeam', 'moonriver', 'celo', 'kava evm', 'fuse', 'mantle']
L2PASS_REFUEL_LIST = {
    'arbitrum':     ['arbitrum nova', 'base', 'gnosis', 'moonbeam', 'moonriver', 'celo', 'kava evm', 'fuse', 'klaytn', 'core', 'opbnb', 'harmony', 'canto'],
    'polygon':      ['arbitrum nova', 'base', 'gnosis', 'moonbeam', 'moonriver', 'celo', 'kava evm', 'fuse', 'klaytn', 'core', 'opbnb', 'harmony', 'canto'],
    'fantom':       ['arbitrum nova', 'base', 'gnosis', 'moonbeam', 'moonriver', 'celo', 'kava evm', 'mantle', 'opbnb', 'harmony', 'canto'],
    'arbitrum nova':['base', 'moonbeam', 'kava evm', 'canto'],
    'base':         ['gnosis', 'moonbeam', 'moonriver', 'kava evm', 'mantle', 'opbnb'],
    'gnosis':       ['moonbeam', 'celo', 'fuse', 'klaytn'],
    'optimism':     ['moonbeam', 'moonriver', 'celo', 'kava evm', 'fuse', 'mantle', 'core', 'opbnb', 'harmony', 'canto'],
    'moonbeam':     ['celo', 'gnosis', 'harmony'],
    'moonriver':    ['kava evm'],
    'celo':         ['fuse', 'moonbeam', 'gnosis'],
    'kava evm':     ['moonriver'],
    'fuse':         ['klaytn', 'opbnb'],
    'klaytn':       ['fuse', 'gnosis'],
    'mantle':       ['klaytn', 'kava evm', 'moonbeam'],
    'bsc':          ['arbitrum nova', 'base', 'gnosis', 'moonbeam', 'moonriver', 'celo', 'kava evm', 'fuse', 'mantle', 'klaytn', 'core', 'opbnb', 'harmony', 'canto'],
}
COUNT_NATIV = [0.0001, 0.0002] #от 0.00001 до 0.00002 нативного токена приемника

MIN_NATIV = {
    'optimism':         0.00008,
    'bsc':              0.0015,
    'arbitrum':         0.00012,
    'polygon':          0.1,
    'celo':             0.1,
    'gnosis':           0.08,
    'moonbeam':         0.3,
    'fantom':           0.15,
    'arbitrum nova':    0.0001,
    'base':             0.0001,
    'moonriver':        0.1,
    'kava evm':         0.3,
    'fuse':             0.7,
    'mantle':           0.2,
    'klaytn':           0.3,
}
