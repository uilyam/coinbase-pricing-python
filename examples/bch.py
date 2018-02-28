from cbp.bch import get_bch_buy, get_bch_sell, get_bch_spot
from cbp.constants import EXCHANGE_RATE_USD

bch_buy_price = get_bch_buy(EXCHANGE_RATE_USD)
bch_sell_price = get_bch_sell(EXCHANGE_RATE_USD)
bch_spot_price = get_bch_spot(EXCHANGE_RATE_USD)

print("Bitcoin Cash Buy Price: ", str(bch_buy_price))
print("Bitcoin Cash Sell Price: ", str(bch_sell_price))
print("Bitcoin Cash Spot Price: ", str(bch_spot_price))
