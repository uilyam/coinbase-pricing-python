from .constants import PRICE_BUY, PRICE_SELL, PRICE_SPOT, CURRENCY_ETH
from .core import get_price

def get_eth_buy(exchange_rate):
    """Get the current Ether Buy price for a given exchange rate.
    
    Arguments:
        exchange_rate {string} -- The supported exchange rate to denominate the price in.
    
    Returns:
        float -- The current Ether Buy price denominated in the provided exchange rate.
    """
    return get_eth(exchange_rate, PRICE_BUY)

def get_eth_spot(exchange_rate):
    """Get the current Ether Spot price for a given exchange rate.
    
    Arguments:
        exchange_rate {string} -- The supported exchange rate to denominate the price in.
    
    Returns:
        float -- The current Ether Spot price denominated in the provided exchange rate.
    """
    return get_eth(exchange_rate, PRICE_SPOT)

def get_eth_sell(exchange_rate):
    """Get the current Ether Sell price for a given exchange rate.
    
    Arguments:
        exchange_rate {string} -- The supported exchange rate to denominate the price in.
    
    Returns:
        float -- The current Ether Sell price denominated in the provided exchange rate.
    """
    return get_eth(exchange_rate, PRICE_SELL)

def get_eth(exchange_rate, price_type):
    """Get the current Ether price for a given price type and in a given exchange rate.
    
    Arguments:
        exchange_rate {string} -- The supported exchange rate to denominate the price in.
        price_type {string} -- The price type to use.
    
    Returns:
        float -- The current Ether price for the given type and denominated in the provided exchange rate.
    """
    return get_price(exchange_rate, price_type, CURRENCY_ETH)
