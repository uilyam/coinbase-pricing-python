from cbp.bulk import get_buy_prices, get_sell_prices, get_spot_prices
from cbp.constants import EXCHANGE_RATE_USD

buy_prices = get_buy_prices(EXCHANGE_RATE_USD)
sell_prices = get_sell_prices(EXCHANGE_RATE_USD)
spot_prices = get_spot_prices(EXCHANGE_RATE_USD)

print("Buy Prices: ", buy_prices)
print("Sell Prices: ", sell_prices)
print("Spot Prices: ", spot_prices)
