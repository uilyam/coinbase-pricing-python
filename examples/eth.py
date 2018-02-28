from cbp.eth import get_eth_buy, get_eth_sell, get_eth_spot
from cbp.constants import EXCHANGE_RATE_USD

eth_buy_price = get_eth_buy(EXCHANGE_RATE_USD)
eth_sell_price = get_eth_sell(EXCHANGE_RATE_USD)
eth_spot_price = get_eth_spot(EXCHANGE_RATE_USD)

print("Ether Buy Price: ", str(eth_buy_price))
print("Ether Sell Price: ", str(eth_sell_price))
print("Ether Spot Price: ", str(eth_spot_price))
