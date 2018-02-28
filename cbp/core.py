import requests
from .utils import format_price_api_url, isolate_amount

def get_price(exchange_rate, price_type, currency):
    """Get the price of a given currency for a given type denominated in a give exchange rate.
    All methods eventually delegate to this method to implement the actually exchange with Coinbase's
    services.

    Arguments:
        exchange_rate {string} -- The exchange rate to denominate the price in.
        price_type {string} -- The supported price type to retrieve.
        currency {string} -- The exchange listed currency to retrieve.
    
    Returns:
        float -- The current currency price for the given type and denominated in the provided exchange rate.
    """
    url = format_price_api_url(exchange_rate, price_type, currency)
    response = requests.get(url)
    price = isolate_amount(response.json())
    return price