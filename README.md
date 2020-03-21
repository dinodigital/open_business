<p align="center" background="black"><img src="un_top.svg" width="450"></p>

<p align="center">
</p>

Python SDK

Ported from official Minter's <a href="https://github.com/MinterTeam/minter-php-sdk">php SDK</a>

Created by <a href="https://www.u-node.net">https://www.u-node.net</a>'s masternode co-founder Roman Matusevich

You can support our project by sending any Minter's coins to our wallet Mx6e0cd64694b1e143adaa7d4914080e748837aec9

Feel free to delegate to our 3% masternode Mp02bc3c3f77d5ab9732ef9fc3801a6d72dc18f88328c14dc735648abfe551f50f


## Installation (так выглядит код)
`pip install minter-sdk`


## SDK use

You can create transaction by import transaction class and create object of this class.

### Create tx

```python
from mintersdk.sdk.transactions import MinterDelegateTx
tx = MinterDelegateTx(pub_key='Mp...', coin='MNT', stake=1, nonce=1, gas_coin='MNT')
```

### Sign tx

``
tx.sign('PRIVATE_KEY')
``

### You can get signed_tx from signed_tx attribute

``
tx.signed_tx
``

To get all required and optional arguments, look for source code.

### To create tx object from raw tx

```python
from mintersdk.sdk.transactions import MinterTx
tx = MinterTx.from_raw(raw_tx='...')
```
You will get tx object of tx type.


### Minter deeplink
Let's create a MinterSendCoinTx
```
from mintersdk.sdk.transactions import MinterSendCoinTx
tx = MinterSendCoinTx(coin='BIP', to='Mx18467bbb64a8edf890201d526c35957d82be3d95', value=1.23456789, nonce=1,
                      gas_coin='MNT', gas_price=1, payload='Hello World')
```

Now it's time to create deeplink
```
from mintersdk.sdk.deeplink import MinterDeeplink
dl = MinterDeeplink(tx=tx, data_only=False)

# Deeplink is generated by all tx params (nonce, gas_price, gas_coin, payload) by default.
# If you want to create deeplink only by tx data, set `data_only=True`
```

After deeplink object is created, you can override it's attributes, e.g.
```
dl = MinterDeeplink(tx=tx)
dl.nonce = ''
dl.gas_coin = 'MNT'
dl.gas_price = 10
```

When your deeplink object is ready, generate it
```
url_link = dl.generate()

# If password check is needed, pass password to generate method
url_link = dl.generate(password='mystrongpassword')
```

Then you might want to create QR-code from your deeplink
```
from mintersdk import MinterHelper
qr_code_filepath = MinterHelper.generate_qr(text=url_link)

# For additional params information for `MinterHelper.generate_qr()`, please see sourcecode for this method.
```
