import unittest
from cbp.utils import format_price_api_url, isolate_amount
from cbp.constants import CURRENCY_BTC, EXCHANGE_RATE_USD, PRICE_BUY

class TestUtils(unittest.TestCase):
    """Unit tests for cbp.utils.py"""

    def test_format_price_api_url_exists(self):
        """Test that the format_price_api_url function exists"""
        self.assertIsNotNone(format_price_api_url)
    
    def test_format_price_api_url_returns_formatted_url(self):
        """Test that the format_price_api_url returns the correct url"""
        expected_url = 'https://api.coinbase.com/v2/prices/buy-BTC/USD'
        url = format_price_api_url(CURRENCY_BTC, EXCHANGE_RATE_USD, PRICE_BUY)
        self.assertEqual(expected_url, url)
    
    def test_isolate_amount(self):
        """Test that the isolate_amount function exists"""
        self.assertIsNotNone(isolate_amount)

    def test_isolate_amount_returns_nested_amount(self):
        """Test that the isolate_amount function returns the nested amount"""
        response = { 'data': { 'amount': '70.2' } }
        amount = isolate_amount(response)
        self.assertEqual(amount, 70.2) 