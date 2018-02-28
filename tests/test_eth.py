import unittest
from unittest.mock import patch
from cbp.eth import get_eth_buy, get_eth_sell, get_eth_spot, get_eth
from cbp.constants import CURRENCY_ETH, EXCHANGE_RATE_USD, PRICE_BUY, PRICE_SELL, PRICE_SPOT

class TestETH(unittest.TestCase):
    """Unit tests for cbp.eth.py"""

    def test_get_eth_exists(self):
        """Test that the get_eth function exists."""
        self.assertIsNotNone(get_eth)

    @patch('cbp.eth.get_price')
    def test_get_eth_calls_get_price(self, get_price_patch):
        """Test get_eth calls get_price with the parameters it is called with plus eth."""
        get_eth(EXCHANGE_RATE_USD, PRICE_BUY)
        get_price_patch.assert_called_with(EXCHANGE_RATE_USD, PRICE_BUY, CURRENCY_ETH)

    @patch('cbp.eth.get_price')
    def test_get_eth_calls_returns_get_price(self, get_price_patch):
        """Test get_eth returns the result of get_price."""
        get_price_patch.return_value = 70.2
        price = get_eth(EXCHANGE_RATE_USD, PRICE_BUY)
        self.assertEqual(price, 70.2)

    def test_get_eth_buy_exists(self):
        """Test that the get_eth_buy function exists."""
        self.assertIsNotNone(get_eth_buy)

    @patch('cbp.eth.get_eth')
    def test_get_eth_buy_calls_get_eth(self, get_eth_patch):
        """Test get_eth_buy calls get_eth with correct parameters."""
        get_eth_buy(EXCHANGE_RATE_USD)
        get_eth_patch.assert_called_with(EXCHANGE_RATE_USD, PRICE_BUY)

    @patch('cbp.eth.get_eth')
    def test_get_eth_buy_returns_get_eth(self, get_eth_patch):
        """Test get_eth_buy returns the value of get_eth."""
        get_eth_patch.return_value = 70.2
        price = get_eth_buy(EXCHANGE_RATE_USD)
        self.assertEqual(price, 70.2)

    def test_get_eth_sell_exists(self):
        """Test that the get_eth_sell function exists."""
        self.assertIsNotNone(get_eth_sell)

    @patch('cbp.eth.get_eth')
    def test_get_eth_sell_calls_get_eth(self, get_eth_patch):
        """Test get_eth_sell calls get_eth with correct parameters."""
        get_eth_sell(EXCHANGE_RATE_USD)
        get_eth_patch.assert_called_with(EXCHANGE_RATE_USD, PRICE_SELL)

    @patch('cbp.eth.get_eth')
    def test_get_eth_sell_returns_get_eth(self, get_eth_patch):
        """Test get_eth_sell returns the value of get_eth."""
        get_eth_patch.return_value = 70.2
        price = get_eth_sell(EXCHANGE_RATE_USD)
        self.assertEqual(price, 70.2)

    def test_get_eth_spot_exists(self):
        """Test that the get_eth_spot function exists."""
        self.assertIsNotNone(get_eth_spot)

    @patch('cbp.eth.get_eth')
    def test_get_eth_spot_calls_get_eth(self, get_eth_patch):
        """Test get_eth_spot calls get_eth with correct parameters."""
        get_eth_spot(EXCHANGE_RATE_USD)
        get_eth_patch.assert_called_with(EXCHANGE_RATE_USD, PRICE_SPOT)

    @patch('cbp.eth.get_eth')
    def test_get_eth_spot_returns_get_eth(self, get_eth_patch):
        """Test get_eth_spot returns the value of get_eth."""
        get_eth_patch.return_value = 70.2
        price = get_eth_spot(EXCHANGE_RATE_USD)
        self.assertEqual(price, 70.2)