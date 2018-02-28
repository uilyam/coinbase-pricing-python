from cbp.bulk import get_spots, get_sells, get_buys
from cbp.constants import EXCHANGE_RATE_USD

spot_prices = get_spots(EXCHANGE_RATE_USD)
sell_prices = get_sells(EXCHANGE_RATE_USD)
buy_prices = get_buys(EXCHANGE_RATE_USD)

print("Spot Prices: ", spot_prices)
print("Sell Prices: ", sell_prices)
print("Buy Prices: ", buy_prices)