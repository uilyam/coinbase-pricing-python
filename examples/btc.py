from cbp.btc import get_btc_buy, get_btc_sell, get_btc_spot
from cbp.constants import EXCHANGE_RATE_USD

btc_buy_price = get_btc_buy(EXCHANGE_RATE_USD)
btc_sell_price = get_btc_sell(EXCHANGE_RATE_USD)
btc_spot_price = get_btc_spot(EXCHANGE_RATE_USD)

print("Bitcoin Buy Price: ", str(btc_buy_price))
print("Bitcoin Sell Price: ", str(btc_sell_price))
print("Bitcoin Spot Price: ", str(btc_spot_price))
