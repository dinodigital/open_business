from mintersdk.minterapi import MinterAPI
from mintersdk.sdk.wallet import MinterWallet

# ----------------------------------------------------------------------------------------------------------------------
# Основные настройки скрипта
# ----------------------------------------------------------------------------------------------------------------------

PAYLOAD = 'Автоматическая выплата'
PAYING_TAXES = True
PAYING_DELEGATORS = False
PAYING_FOUNDERS = True


# ----------------------------------------------------------------------------------------------------------------------
# Настройки выплат
# ----------------------------------------------------------------------------------------------------------------------

# НАЛОГИ
TAXES = {
    'Mx0f4e09ae5e998cf0322f1f13b36284274b5a3db5': 0.1
}

# ДЕЛЕГАТОРЫ
DELEGATORS_PERCENT = 0.1
DELEGATED_TOKEN = 'GORBUNOV'
MIN_COINS_DELEGATED = 1
STOP_LIST = ['Mx0f4e09ae5e998cf0322f1f13b36284274b5a3db5']

# ОСНОВАТЕЛИ
FOUNDERS = {
    'Mx0f4e09ae5e998cf0322f1f13b36284274b5a3db5': 0.85,
    'Mx5cef09065d68561ad9f61a905c7d0aa230117733': 0.15
}

# FOUNDERS = {
#         'gorbunov': {
#             'wallet': 'Mx0f4e09ae5e998cf0322f1f13b36284274b5a3db5',
#             'percent': 0.85},
#         'isheldon': {
#             'wallet': 'Mx5cef09065d68561ad9f61a905c7d0aa230117733',
#             'percent': 0.15}
# }


# ----------------------------------------------------------------------------------------------------------------------
# Настройки API
# ----------------------------------------------------------------------------------------------------------------------
NODE_API_URL = 'http://api.minter.one'
TIMEOUTS = {'read_timeout': 6, 'connect_timeout': 7}
API = MinterAPI(NODE_API_URL, **TIMEOUTS)


# ----------------------------------------------------------------------------------------------------------------------
# Автонастройки кошелька
# ----------------------------------------------------------------------------------------------------------------------
with open('script/seed.txt', 'r') as f:
    SEED = f.read()
PRIVATE_KEY = MinterWallet.create(mnemonic=SEED)['private_key']
ADDRESS = MinterWallet.create(mnemonic=SEED)['address']

