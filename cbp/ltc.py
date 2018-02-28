from .constants import PRICE_BUY, PRICE_SELL, PRICE_SPOT, CURRENCY_LTC
from .core import get_price

def get_ltc_buy(exchange_rate):
    """Get the current Litecoin Buy price for a given exchange rate.
    
    Arguments:
        exchange_rate {string} -- The supported exchange rate to denominate the price in.
    
    Returns:
        float -- The current Litecoin Buy price denominated in the provided exchange rate.
    """
    return get_ltc(exchange_rate, PRICE_BUY)

def get_ltc_spot(exchange_rate):
    """Get the current Litecoin Spot price for a given exchange rate.
    
    Arguments:
        exchange_rate {string} -- The supported exchange rate to denominate the price in.
    
    Returns:
        float -- The current Litecoin Spot price denominated in the provided exchange rate.
    """
    return get_ltc(exchange_rate, PRICE_SPOT)

def get_ltc_sell(exchange_rate):
    """Get the current Litecoin Sell price for a given exchange rate.
    
    Arguments:
        exchange_rate {string} -- The supported exchange rate to denominate the price in.
    
    Returns:
        float -- The current Litecoin Sell price denominated in the provided exchange rate.
    """
    return get_ltc(exchange_rate, PRICE_SELL)

def get_ltc(exchange_rate, price_type):
    """Get the current Litecoin price for a given price type and in a given exchange rate.
    
    Arguments:
        exchange_rate {string} -- The supported exchange rate to denominate the price in.
        price_type {string} -- The price type to use.
    
    Returns:
        float -- The current Litecoin price for the given type and denominated in the provided exchange rate.
    """
    return get_price(exchange_rate, price_type, CURRENCY_LTC)
