from .btc import get_btc_buy, get_btc_sell, get_btc_spot
from .bch import get_bch_buy, get_bch_sell, get_bch_spot
from .eth import get_eth_buy, get_eth_sell, get_eth_spot
from .ltc import get_ltc_buy, get_ltc_sell, get_ltc_spot

from .constants import CURRENCY_BTC, CURRENCY_BCH, CURRENCY_ETH, CURRENCY_LTC

def get_buy_prices(exchange_rate):
    """Get the current buy prices for all supported currencies on Coinbase denominated
    in the provided exchange rate.
    
    Arguments:
        exchange_rate {string} -- The exchange rate to denominate the prices in.
    
    Returns:
        dict -- A dictionary map of currencies to their float buy price. 
    """
    prices = {}
    prices[CURRENCY_BTC] = get_btc_buy(exchange_rate)
    prices[CURRENCY_BCH] = get_bch_buy(exchange_rate)
    prices[CURRENCY_ETH] = get_eth_buy(exchange_rate)
    prices[CURRENCY_LTC] = get_ltc_buy(exchange_rate)
    return prices

def get_sell_prices(exchange_rate):
    """Get the current sell prices for all supported currencies on Coinbase denominated
    in the provided exchange rate.
    
    Arguments:
        exchange_rate {string} -- The exchange rate to denominate the prices in.
    
    Returns:
        dict -- A dictionary map of currencies to their float sell price. 
    """
    prices = {}
    prices[CURRENCY_BTC] = get_btc_sell(exchange_rate)
    prices[CURRENCY_BCH] = get_bch_sell(exchange_rate)
    prices[CURRENCY_ETH] = get_eth_sell(exchange_rate)
    prices[CURRENCY_LTC] = get_ltc_sell(exchange_rate)
    return prices

def get_spot_prices(exchange_rate):
    """Get the current spot prices for all supported currencies on Coinbase denominated
    in the provided exchange rate.
    
    Arguments:
        exchange_rate {string} -- The exchange rate to denominate the prices in.
    
    Returns:
        dict -- A dictionary map of currencies to their float spot price. 
    """
    prices = {}
    prices[CURRENCY_BTC] = get_btc_spot(exchange_rate)
    prices[CURRENCY_BCH] = get_bch_spot(exchange_rate)
    prices[CURRENCY_ETH] = get_eth_spot(exchange_rate)
    prices[CURRENCY_LTC] = get_ltc_spot(exchange_rate)
    return prices