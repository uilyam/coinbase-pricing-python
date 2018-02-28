from cbp.ltc import get_ltc_buy, get_ltc_sell, get_ltc_spot
from cbp.constants import EXCHANGE_RATE_USD

ltc_buy_price = get_ltc_buy(EXCHANGE_RATE_USD)
ltc_sell_price = get_ltc_sell(EXCHANGE_RATE_USD)
ltc_spot_price = get_ltc_spot(EXCHANGE_RATE_USD)

print("Litecoin Buy Price: ", str(ltc_buy_price))
print("Litecoin Sell Price: ", str(ltc_sell_price))
print("Litecoin Spot Price: ", str(ltc_spot_price))
