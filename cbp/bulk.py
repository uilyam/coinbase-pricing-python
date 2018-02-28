from .btc import get_btc_buy, get_btc_sell, get_btc_spot
from .constants import CURRENCY_BTC

def get_spots(exchange_rate):
    """Get the current spot prices for all supported currencies on Coinbase denominated
    in the provided exchange rate.
    
    Arguments:
        exchange_rate {string} -- The exchange rate to denominate the prices in.
    
    Returns:
        dict -- A dictionary map of currencies to their float spot price. 
    """
    prices = {}
    prices[CURRENCY_BTC] = get_btc_spot(exchange_rate)
    return prices

def get_sells(exchange_rate):
    """Get the current sell prices for all supported currencies on Coinbase denominated
    in the provided exchange rate.
    
    Arguments:
        exchange_rate {string} -- The exchange rate to denominate the prices in.
    
    Returns:
        dict -- A dictionary map of currencies to their float sell price. 
    """
    prices = {}
    prices[CURRENCY_BTC] = get_btc_sell(exchange_rate)
    return prices

def get_buys(exchange_rate):
    """Get the current buy prices for all supported currencies on Coinbase denominated
    in the provided exchange rate.
    
    Arguments:
        exchange_rate {string} -- The exchange rate to denominate the prices in.
    
    Returns:
        dict -- A dictionary map of currencies to their float buy price. 
    """
    prices = {}
    prices[CURRENCY_BTC] = get_btc_buy(exchange_rate)
    return prices