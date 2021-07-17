"""
File:  super_simple_stockes.py
Created By:  Nimisha Thekkarath(nimisha0092@gmail.com)
"""
import enum
import operator

from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from functools import reduce


@enum.unique
class StockSymbol(enum.Enum):
    """unique isdentifier for each stocks"""
    TEA=1
    POP=2
    ALE=3
    GIN=4
    JOE=5

@enum.unique
class BuyOrSell(enum.Enum):
    """Indicator to represent buying or selling the trade"""
    BUY=1
    SELL=2

class Trade:
    """The Trade class will collect all the details retaled to the Trade"""
    def __init__(self,
                 stock_symbol: StockSymbol,
                 timestamp: datetime,
                 quantity: int,
                 price_per_share: float,
                 buyorsell: BuyOrSell):  
        """
        :parram stock_symbol: TEA,POP,ALE,GIN or JOE
        :parram timestamp: The moment when the transaction has taken place
        :parram quantity: Amount of shares 
        :parram price_per_share: Price for each share
        :parram buyorsell: Indication to buy or sell
        """     

        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("quantity of the share should be positive")

        if  price_per_share >= 0:
            self.price_per_share = price_per_share
        else:
            raise ValueError("price per share should be positive") 

        self.stock_symbol = stock_symbol
        self.timestamp = timestamp
        self.buyorsell = buyorsell 

        @property
        def total_price(self) -> float:
            """
            :return: Total price of the trade
            """
            return self.quantity * self.price_per_share

class Stock(ABC):
    """
    This is an abstract class for CommonStock and PrefferedStock.
    It has an abstract method 'dividend'.
    It has common interfaces that both common and preferred stocks share.

    ..note:: The class variable Stock.price_time_interval is the length of the time interval that is significant to calculate the stock
        price.
    """   
    price_time_interval = timedelta(minutes=15)   

    def __init__(self,
                stock_symbol:StockSymbol,
                par_value:float):
        """
        :parram stock_symbol: The stock_symbol that identifies this stock(TEA,POP,ALE,GIN or JOE )
        :param par_value: The par value per share for this stock

        .. note:: This initializer also creates the instance variable self.trades,
            which is to hold a list of recorded instances of Trade.
        """
        
        self.stock_symbol = stock_symbol
        self.par_value = par_value

        self.trades = []

    def record_trade(self, trade: Trade):
        """Records a trade for this stock.
        :param trade: The trade to be recorded
        :raise TypeError: If the instance is not Trade the raise TypeError
        :raise ValueError: Checks the stock_symbol of the trade 
        """
        if not isinstance(trade, Trade):
            raise TypeError("Argument trade={trade} should be of type Trade.".format(trade=trade))
        elif self.stock_symbol is not trade.stock_symbol:
            raise ValueError("Argument trade={trade} does not belong to this stock.".format(trade=trade))
        else:
            self.trades.append(trade)    

    @property
    @abstractmethod
    def dividend(self)-> float:
        """
        :retuen: The dividend for the given stock
        """
        pass

    @property
    def stock_price(self) -> float:
        """self.trades
        :return: The price per share for the last recorded trade for this stock
        :raise AttributeError:
        .. note:: First we will sort the trade according to the timestamp,
           then we will take the latest price of the stock.
        """
        if len(self.trades) > 0:
            by_timestamp = sorted(self.trades,
                                  key=lambda trade: trade.timestamp,
                                  reverse=True)
            return by_timestamp[0].price_per_share
        else:
            raise AttributeError("The last stock price is not yet available.")

    @property
    def dividend_yield(self) -> float:
        return self.dividend / self.stock_price

    @property
    def price_earnings_ratio(self) -> float:
        """
        :return: The P/E ratio for this stock
        """
        if self.dividend != 0:
            return self.stock_price / self.dividend
        else:
            return None    

    def price(self,
              current_time: datetime=datetime.now()) -> float:
        """
        :param current_time: The Current time.
        :return: The average price per share based on trades recorded in the last
            Stock.price_time_interval. None if there are 0 trades that satisfy this
            condition.
        
        """
        """collect the trades that happend in this perticular span of time in to significant_trades""" 
        significant_trades = [trade for trade in self.trades
                              if trade.timestamp >= current_time - self.price_time_interval]

        if len(significant_trades) > 0:
            trade_prices = (trade.total_price for trade in significant_trades)
            quantities = (trade.quantity for trade in significant_trades)
            return sum(trade_prices) / sum(quantities)
        else:
            return None
  
class CommonStock(Stock):
    """Common Stock"""

    def __init__(self,
                stock_symbol:StockSymbol,
                par_value:float,
                last_dividend: float):
        """
        :param last_dividend: Last dividend of the given stock 
        """   
        super().__init__(stock_symbol, par_value)
        self.last_dividend = last_dividend 

    @property
    def dividend(self):
        return self.last_dividend

class PreferredStock(Stock):
    """Preferred Stock"""

    def __init__(self,
                stock_symbol: StockSymbol,
                par_value: float,
                fixed_dividend: float):
        """
        :param fixed_dividend: A decimal number that expresses the fixed dividend
            as a ratio of the face value of each share.
        """

        super().__init__(stock_symbol, par_value)
        self.fixed_dividend = fixed_dividend

    @property
    def dividend(self):
        return self.fixed_dividend * self.par_value  

class GlobalBeverageCorporationExchange:

    """The whole exchange where the trades take place"""

    def __init__(self,
                  stocks: [Stock] ):
        """
        :param stocks: The stocks traded at this exchange.
        :raise ValueError:
        """
        if len(stocks) > 0:
            self.stocks = stocks
        else:
            raise ValueError("Argument stocks={stocks} should be a non empty sequence.".format(stocks=stocks))

    def record_trade(self,
                     trade: Trade):
        """Records a trade for the proper stock.
        :param trade: The trade to record.
        """
        stock = next(stock for stock in self.stocks
                     if stock.stock_symbol is trade.stock_symbol)
        stock.record_trade(trade)

    def geometric_mean(self,
                        current_time: datetime=datetime.now()) -> float:
        """
        :param current_time: The point of time for which we want to obtain the index.
        :return: The geometric mean of all stock prices. Returns None if any of them is
            None.
        """
        n = len(self.stocks)
        stock_prices = [stock.price(current_time) for stock in self.stocks]

        if None in stock_prices:
            return None
        else:
            product = reduce(operator.mul, stock_prices, 1)
            return product**(1/n)

   




