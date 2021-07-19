# Super Simple Stocks

This code is submitted as an answer to the assignment Super Simple Stocks included in the hiring process for the position JP Morgan - 210115193 - Python Software Engineer - Complex Assets. Its instructions can be found in the document docks/Candidate_tech_programming_test.docx.

## Requirements

The application has been developed using Python 3 (3.9.6). This is a new project from scratch, and no third-party libraries are needed.

## Code structure and usage

All the application proper is fully contained in the single top-level module `super_simple_stocks`. It is to be used by packing a set of instances of `Stock` in a sequence and pass it as the only argument to `GlobalBeverageCorporationExchange` initializer. The resulting instance is to be used a a representation of the complete GBCE. 

`Stock` itself is abstract, objects may only be created by means of its two inheriting classes, `CommonStock` and `PreferredStock`.

From that point on the method `GlobalBeverageCorporationExchange.record_trade` may be used to record new trades.

The calculations requested in the assignment instructions are then supplied by the following properties or methods:

- For a given instance of `Stock`:
  - _Calculate the dividend yield_: `Stock.dividend_yield`
  - _Calculate the P/E Ratio_: `Stock.price_earnings_ratio`
  - _Record a trade, with timestamp, quantity of shares, buy or sell indicator and price_: Create an instance of `Trade` and supply it to an instance of`GlobalBeverageCorporationExchange` that contains the proper stock my means of `record_trade`
  - _Calculate Stock Price based on trades recorded in past 15 minutes_: `Stock.price`
- _Calculate the GBCE All Share Index using the geometric mean of prices for all stocks_: `GlobalBeverageCorporationExchange.geometric_mean`.

Type hints are present in all relevant signatures and basic documentation is included in the code itself.

## OOPS Concepts included in this project

This project source code is sutable for forming part of the object module of production application
It includes the bellow OOPS Concepts.

- Class : This project has Class like Trade,Stock,CommonStock,PreferredStock and GlobalBeverageCorporationExchange. Here Stock is an abstract class for CommonStock and PreferredStock, Stock servers as a super class for these two classes.
- Inheritance: Stock class servers as a super class for CommonStock and PreferredStock classes.
- Data Encapsulation: @property is an inbuilt-python decorator and its mainly used to increase data encapsulation.
- The code is making use of the other OOPS concepts like 
   - Method
   - Object
   - Data abstraction
   - Polimorphism
 - I have included `loggers` and `exception handling`  also.


## Tests

A moderately extensive suite of tests is included in `tests/`. The autodiscovery feature of `unittest` makes it fairly convenient to run them by executing the following command:
 ````
$ git clone https://github.com/nimishathekkarath/super_simple_stocks.git
$ cd super_simple_stocks/
$ python -m unittest -v
````
The `-v` switch is optional and it stands for its verbose mode.





