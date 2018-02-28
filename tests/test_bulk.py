import unittest
from unittest.mock import patch
from cbp.bulk import get_buy_prices, get_sell_prices, get_spot_prices
from cbp.constants import EXCHANGE_RATE_USD, CURRENCY_BTC, CURRENCY_BCH, CURRENCY_ETH, CURRENCY_LTC
class TestBulk(unittest.TestCase):
    """Unit tests for cbp.bulk.py"""

    def test_get_buy_prices_exists(self): 
        """Test that the bulk get_buy_prices function exists."""
        self.assertIsNotNone(get_buy_prices)

    @patch('cbp.bulk.get_ltc_buy')
    @patch('cbp.bulk.get_eth_buy')
    @patch('cbp.bulk.get_bch_buy')
    @patch('cbp.bulk.get_btc_buy')
    def test_get_buy_prices_returns_complete_dictionary(self, get_btc_buy_patched, get_bch_buy_patched, get_eth_buy_patched, get_ltc_buy_patched):
        """Test that the get_buy_prices returns a dictionary with each supported currency."""
        get_btc_buy_patched.return_value = 1.1
        get_bch_buy_patched.return_value = 1.2
        get_eth_buy_patched.return_value = 1.3
        get_ltc_buy_patched.return_value = 1.4
        expected_result = {
            CURRENCY_BTC: 1.1,
            CURRENCY_BCH: 1.2,
            CURRENCY_ETH: 1.3,
            CURRENCY_LTC: 1.4
        }
        result = get_buy_prices(EXCHANGE_RATE_USD)
        self.assertEqual(expected_result, result)

    def test_get_sell_prices_exists(self): 
        """Test that the bulk get_sell_prices function exists."""
        self.assertIsNotNone(get_sell_prices)

    @patch('cbp.bulk.get_ltc_sell')
    @patch('cbp.bulk.get_eth_sell')
    @patch('cbp.bulk.get_bch_sell')
    @patch('cbp.bulk.get_btc_sell')
    def test_get_sell_prices_returns_complete_dictionary(self, get_btc_sell_patched, get_bch_sell_patched, get_eth_sell_patched, get_ltc_sell_patched):
        """Test that the get_sell_prices returns a dictionary with each supported currency."""
        get_btc_sell_patched.return_value = 1.1
        get_bch_sell_patched.return_value = 1.2
        get_eth_sell_patched.return_value = 1.3
        get_ltc_sell_patched.return_value = 1.4
        expected_result = {
            CURRENCY_BTC: 1.1,
            CURRENCY_BCH: 1.2,
            CURRENCY_ETH: 1.3,
            CURRENCY_LTC: 1.4
        }
        result = get_sell_prices(EXCHANGE_RATE_USD)
        self.assertEqual(expected_result, result)

    def test_get_spot_prices_exists(self): 
        """Test that the bulk get_spot_prices function exists."""
        self.assertIsNotNone(get_spot_prices)

    @patch('cbp.bulk.get_ltc_spot')
    @patch('cbp.bulk.get_eth_spot')
    @patch('cbp.bulk.get_bch_spot')
    @patch('cbp.bulk.get_btc_spot')
    def test_get_spot_prices_returns_complete_dictionary(self, get_btc_spot_patched, get_bch_spot_patched, get_eth_spot_patched, get_ltc_spot_patched):
        """Test that the get_spot_prices returns a dictionary with each supported currency."""
        get_btc_spot_patched.return_value = 1.1
        get_bch_spot_patched.return_value = 1.2
        get_eth_spot_patched.return_value = 1.3
        get_ltc_spot_patched.return_value = 1.4
        expected_result = {
            CURRENCY_BTC: 1.1,
            CURRENCY_BCH: 1.2,
            CURRENCY_ETH: 1.3,
            CURRENCY_LTC: 1.4
        }
        result = get_spot_prices(EXCHANGE_RATE_USD)
        self.assertEqual(expected_result, result)
