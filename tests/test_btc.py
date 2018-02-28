import unittest
from unittest.mock import patch
from cbp.btc import get_btc_buy, get_btc_sell, get_btc_spot, get_btc
from cbp.constants import CURRENCY_BTC, EXCHANGE_RATE_USD, PRICE_BUY, PRICE_SELL, PRICE_SPOT

class TestBTC(unittest.TestCase):
    """Unit tests for cbp.btc.py"""

    def test_get_btc_exists(self):
        """Test that the get_btc function exists"""
        self.assertIsNotNone(get_btc)

    @patch('cbp.btc.get_price')
    def test_get_btc_calls_get_price(self, get_price_patch):
        """Test get_btc calls get_price with the parameters it is called with plus BTC."""
        get_btc(EXCHANGE_RATE_USD, PRICE_BUY)
        get_price_patch.assert_called_with(EXCHANGE_RATE_USD, PRICE_BUY, CURRENCY_BTC)

    @patch('cbp.btc.get_price')
    def test_get_btc_calls_returns_get_price(self, get_price_patch):
        """Test get_btc returns the result of get_price."""
        get_price_patch.return_value = 70.2
        price = get_btc(EXCHANGE_RATE_USD, PRICE_BUY)
        self.assertEqual(price, 70.2)

    def test_get_btc_buy_exists(self):
        """Test that the get_btc_buy function exists"""
        self.assertIsNotNone(get_btc_buy)

    @patch('cbp.btc.get_btc')
    def test_get_btc_buy_calls_get_btc(self, get_btc_patch):
        """Test get_btc_buy calls get_btc with correct parameters."""
        get_btc_buy(EXCHANGE_RATE_USD)
        get_btc_patch.assert_called_with(EXCHANGE_RATE_USD, PRICE_BUY)

    @patch('cbp.btc.get_btc')
    def test_get_btc_buy_returns_get_btc(self, get_btc_patch):
        """Test get_btc_buy returns the value of get_btc"""
        get_btc_patch.return_value = 70.2
        price = get_btc_buy(EXCHANGE_RATE_USD)
        self.assertEqual(price, 70.2)

    def test_get_btc_sell_exists(self):
        """Test that the get_btc_sell function exists"""
        self.assertIsNotNone(get_btc_sell)

    @patch('cbp.btc.get_btc')
    def test_get_btc_sell_calls_get_btc(self, get_btc_patch):
        """Test get_btc_sell calls get_btc with correct parameters."""
        get_btc_sell(EXCHANGE_RATE_USD)
        get_btc_patch.assert_called_with(EXCHANGE_RATE_USD, PRICE_SELL)

    @patch('cbp.btc.get_btc')
    def test_get_btc_sell_returns_get_btc(self, get_btc_patch):
        """Test get_btc_sell returns the value of get_btc"""
        get_btc_patch.return_value = 70.2
        price = get_btc_sell(EXCHANGE_RATE_USD)
        self.assertEqual(price, 70.2)

    def test_get_btc_spot_exists(self):
        """Test that the get_btc_spot function exists"""
        self.assertIsNotNone(get_btc_spot)

    @patch('cbp.btc.get_btc')
    def test_get_btc_spot_calls_get_btc(self, get_btc_patch):
        """Test get_btc_spot calls get_btc with correct parameters."""
        get_btc_spot(EXCHANGE_RATE_USD)
        get_btc_patch.assert_called_with(EXCHANGE_RATE_USD, PRICE_SPOT)

    @patch('cbp.btc.get_btc')
    def test_get_btc_spot_returns_get_btc(self, get_btc_patch):
        """Test get_btc_spot returns the value of get_btc"""
        get_btc_patch.return_value = 70.2
        price = get_btc_spot(EXCHANGE_RATE_USD)
        self.assertEqual(price, 70.2)