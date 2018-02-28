from .constants import  API_PROTOCOL, API_VERSION, API_HOSTNAME, API_ENDPOINT_PRICE, API_RESPONSE_DATA, API_RESPONSE_AMOUNT

def format_price_api_url(exchange_rate, price_type, currency):
    """Format the url for a request to the price API.
    
    Arguments:
        exchange_rate {string} -- The exchange rate to denominate the price in.
        price_type {string} -- The supported price type to retrieve.
        currency {string} -- The exchange listed currency to retrieve.
    
    Returns:
        string -- The formatted url to use for an API request.
    """
    return "{0}://{1}/{2}/{3}/{4}-{5}/{6}".format(API_PROTOCOL, API_HOSTNAME, API_VERSION, API_ENDPOINT_PRICE, currency, exchange_rate, price_type)

def isolate_amount(response_obj):
    """Isolate the "amount" or price value in a response object returned by the API.
    
    Arguments:
        response_obj {dict} -- The response object (dict) returned from the Coinbase API.
        It will contain a nested property for the amount value.

    Returns:
        string -- The formatted url to use for an API request.
    """
    return float(response_obj[API_RESPONSE_DATA][API_RESPONSE_AMOUNT])