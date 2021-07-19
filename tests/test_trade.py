import unittest

from super_simple_stocks import Trade
from .factories import TradeFactory


class TradeInitTestCase(unittest.TestCase):

    def setUp(self):
        self.trade = TradeFactory.get_trade()

    def test_raises_value_error_on_non_positive_qty(self):
        with self.assertRaises(ValueError):
            bad_trade = Trade(ticker_symbol=self.trade.ticker_symbol,
                              timestamp=self.trade.timestamp,
                              quantity=0,
                              price_per_share=self.trade.price_per_share,
                              buyorsell=self.trade.buyorsell)

    def test_raises_value_error_on_negative_price_per_share(self):
        with self.assertRaises(ValueError):
            bad_trade = Trade(ticker_symbol=self.trade.ticker_symbol,
                              timestamp=self.trade.timestamp,
                              quantity=self.trade.quantity,
                              price_per_share=-25.0,
                              buyorsell=self.trade.buyorsell)


class TradeTotalPriceTestCase(unittest.TestCase):

    def test_total_price_value(self):

        trade = TradeFactory.get_trade()
        expected_value = trade.quantity * trade.price_per_share
        self.assertEqual(trade.total_price, expected_value)