from cbp.utils import format_price_api_url, isolate_amount
from cbp.constants import EXCHANGE_RATE_USD, PRICE_SPOT, CURRENCY_BTC

btc_spot_usd_price_url = format_price_api_url(EXCHANGE_RATE_USD, PRICE_SPOT, CURRENCY_BTC)
print('Formatted URL: ', btc_spot_usd_price_url)

response = { 'data': { 'amount': '70.2' } }
amount = isolate_amount(response)
print('Isolated Amount: ', amount)