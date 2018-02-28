from .constants import PRICE_BUY, PRICE_SELL, PRICE_SPOT, CURRENCY_BCH
from .core import get_price

def get_bch_buy(exchange_rate):
    """Get the current Bitcoin Cash Buy price for a given exchange rate.
    
    Arguments:
        exchange_rate {string} -- The supported exchange rate to denominate the price in.
    
    Returns:
        float -- The current Bitcoin Cash Buy price denominated in the provided exchange rate.
    """
    return get_bch(exchange_rate, PRICE_BUY)

def get_bch_spot(exchange_rate):
    """Get the current Bitcoin Cash Spot price for a given exchange rate.
    
    Arguments:
        exchange_rate {string} -- The supported exchange rate to denominate the price in.
    
    Returns:
        float -- The current Bitcoin Cash Spot price denominated in the provided exchange rate.
    """
    return get_bch(exchange_rate, PRICE_SPOT)

def get_bch_sell(exchange_rate):
    """Get the current Bitcoin Cash Sell price for a given exchange rate.
    
    Arguments:
        exchange_rate {string} -- The supported exchange rate to denominate the price in.
    
    Returns:
        float -- The current Bitcoin Cash Sell price denominated in the provided exchange rate.
    """
    return get_bch(exchange_rate, PRICE_SELL)

def get_bch(exchange_rate, price_type):
    """Get the current Bitcoin Cash price for a given price type and in a given exchange rate.
    
    Arguments:
        exchange_rate {string} -- The supported exchange rate to denominate the price in.
        price_type {string} -- The price type to use.
    
    Returns:
        float -- The current Bitcoin Cash price for the given type and denominated in the provided exchange rate.
    """
    return get_price(exchange_rate, price_type, CURRENCY_BCH)
