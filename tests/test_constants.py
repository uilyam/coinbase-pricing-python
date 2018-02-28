import unittest
from unittest.mock import patch
import cbp.constants as constants


class TestConstants(unittest.TestCase):
    """Unit tests for cbp.constants.py"""

    def test_constants_module_exposes_constants(self):
        """Test that the constants module exposes constants"""
        self.assertIsNotNone(constants.API_VERSION)
        self.assertIsNotNone(constants.API_PROTOCOL)
        self.assertIsNotNone(constants.API_HOSTNAME)
        self.assertIsNotNone(constants.API_ENDPOINT_PRICE)
        self.assertIsNotNone(constants.API_RESPONSE_DATA)
        self.assertIsNotNone(constants.API_RESPONSE_AMOUNT)
        self.assertIsNotNone(constants.PRICE_BUY)
        self.assertIsNotNone(constants.PRICE_SELL)
        self.assertIsNotNone(constants.PRICE_SPOT)
        self.assertIsNotNone(constants.CURRENCY_BTC)
        self.assertIsNotNone(constants.CURRENCY_BCH)
        self.assertIsNotNone(constants.CURRENCY_ETH)
        self.assertIsNotNone(constants.CURRENCY_LTC)
        self.assertIsNotNone(constants.EXCHANGE_RATE_USD)