import unittest
from unittest.mock import patch
from cbp.ltc import get_ltc_buy, get_ltc_sell, get_ltc_spot, get_ltc
from cbp.constants import CURRENCY_LTC, EXCHANGE_RATE_USD, PRICE_BUY, PRICE_SELL, PRICE_SPOT

class TestLTC(unittest.TestCase):
    """Unit tests for cbp.ltc.py"""

    def test_get_ltc_exists(self):
        """Test that the get_ltc function exists."""
        self.assertIsNotNone(get_ltc)

    @patch('cbp.ltc.get_price')
    def test_get_ltc_calls_get_price(self, get_price_patch):
        """Test get_ltc calls get_price with the parameters it is called with plus ltc."""
        get_ltc(EXCHANGE_RATE_USD, PRICE_BUY)
        get_price_patch.assert_called_with(EXCHANGE_RATE_USD, PRICE_BUY, CURRENCY_LTC)

    @patch('cbp.ltc.get_price')
    def test_get_ltc_calls_returns_get_price(self, get_price_patch):
        """Test get_ltc returns the result of get_price."""
        get_price_patch.return_value = 70.2
        price = get_ltc(EXCHANGE_RATE_USD, PRICE_BUY)
        self.assertEqual(price, 70.2)

    def test_get_ltc_buy_exists(self):
        """Test that the get_ltc_buy function exists."""
        self.assertIsNotNone(get_ltc_buy)

    @patch('cbp.ltc.get_ltc')
    def test_get_ltc_buy_calls_get_ltc(self, get_ltc_patch):
        """Test get_ltc_buy calls get_ltc with correct parameters."""
        get_ltc_buy(EXCHANGE_RATE_USD)
        get_ltc_patch.assert_called_with(EXCHANGE_RATE_USD, PRICE_BUY)

    @patch('cbp.ltc.get_ltc')
    def test_get_ltc_buy_returns_get_ltc(self, get_ltc_patch):
        """Test get_ltc_buy returns the value of get_ltc."""
        get_ltc_patch.return_value = 70.2
        price = get_ltc_buy(EXCHANGE_RATE_USD)
        self.assertEqual(price, 70.2)

    def test_get_ltc_sell_exists(self):
        """Test that the get_ltc_sell function exists."""
        self.assertIsNotNone(get_ltc_sell)

    @patch('cbp.ltc.get_ltc')
    def test_get_ltc_sell_calls_get_ltc(self, get_ltc_patch):
        """Test get_ltc_sell calls get_ltc with correct parameters."""
        get_ltc_sell(EXCHANGE_RATE_USD)
        get_ltc_patch.assert_called_with(EXCHANGE_RATE_USD, PRICE_SELL)

    @patch('cbp.ltc.get_ltc')
    def test_get_ltc_sell_returns_get_ltc(self, get_ltc_patch):
        """Test get_ltc_sell returns the value of get_ltc."""
        get_ltc_patch.return_value = 70.2
        price = get_ltc_sell(EXCHANGE_RATE_USD)
        self.assertEqual(price, 70.2)

    def test_get_ltc_spot_exists(self):
        """Test that the get_ltc_spot function exists."""
        self.assertIsNotNone(get_ltc_spot)

    @patch('cbp.ltc.get_ltc')
    def test_get_ltc_spot_calls_get_ltc(self, get_ltc_patch):
        """Test get_ltc_spot calls get_ltc with correct parameters."""
        get_ltc_spot(EXCHANGE_RATE_USD)
        get_ltc_patch.assert_called_with(EXCHANGE_RATE_USD, PRICE_SPOT)

    @patch('cbp.ltc.get_ltc')
    def test_get_ltc_spot_returns_get_ltc(self, get_ltc_patch):
        """Test get_ltc_spot returns the value of get_ltc."""
        get_ltc_patch.return_value = 70.2
        price = get_ltc_spot(EXCHANGE_RATE_USD)
        self.assertEqual(price, 70.2)