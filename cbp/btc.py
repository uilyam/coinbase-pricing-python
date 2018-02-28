from .constants import PRICE_BUY, PRICE_SELL, PRICE_SPOT, CURRENCY_BTC
from .core import get_price

def get_btc_buy(exchange_rate):
    """Get the current Bitcoin Buy price for a given exchange rate.
    
    Arguments:
        exchange_rate {string} -- The supported exchange rate to denominate the price in.
    
    Returns:
        float -- The current Bitcoin Buy price denominated in the provided exchange rate.
    """
    return get_btc(exchange_rate, PRICE_BUY)

def get_btc_spot(exchange_rate):
    """Get the current Bitcoin Spot price for a given exchange rate.
    
    Arguments:
        exchange_rate {string} -- The supported exchange rate to denominate the price in.
    
    Returns:
        float -- The current Bitcoin Spot price denominated in the provided exchange rate.
    """
    return get_btc(exchange_rate, PRICE_SPOT)

def get_btc_sell(exchange_rate):
    """Get the current Bitcoin Buy price for a given exchange rate.
    
    Arguments:
        exchange_rate {string} -- The supported exchange rate to denominate the price in.
    
    Returns:
        float -- The current Bitcoin Sell price denominated in the provided exchange rate.
    """
    return get_btc(exchange_rate, PRICE_SELL)

def get_btc(exchange_rate, price_type):
    """Get the current Bitcoin price for a given price type and in a given exchange rate.
    
    Arguments:
        exchange_rate {string} -- The supported exchange rate to denominate the price in.
        price_type {string} -- The price type to use.
    
    Returns:
        float -- The current Bitcoin price for the given type and denominated in the provided exchange rate.
    """
    return get_price(exchange_rate, price_type, CURRENCY_BTC)
