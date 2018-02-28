import unittest
from unittest.mock import patch, MagicMock
from cbp.core import get_price
from cbp.utils import format_price_api_url
from cbp.constants import CURRENCY_BTC, EXCHANGE_RATE_USD, PRICE_BUY

class TestCore(unittest.TestCase):
    """Unit tests for cbp.core.py"""

    def test_get_price_exists(self):
        """Test that the get_price function exists"""
        self.assertIsNotNone(get_price)

    @patch('cbp.core.requests')
    def test_get_price_calls_request_with_proper_url(self, requests_patch):
        """Test that proper url is provided to the requests.get method."""
        url_to_call_with = format_price_api_url(EXCHANGE_RATE_USD, PRICE_BUY, CURRENCY_BTC)
        get_price(EXCHANGE_RATE_USD, PRICE_BUY, CURRENCY_BTC)
        requests_patch.get.assert_called_with(url_to_call_with)

    @patch('cbp.core.requests')
    def test_get_price_returns_float(self, requests_patch):
        """Test that get_price returns the price as a float."""
        get_mock = MagicMock()
        get_mock.json.return_value = { 'data': { 'amount': '72.1' } }
        requests_patch.get.return_value = get_mock
        price = get_price(EXCHANGE_RATE_USD, PRICE_BUY, CURRENCY_BTC)
        self.assertEqual(price, 72.1)
