## trades
A package to aid stock traders make quick decisions.

It contains the following:
1. Computes momentum for stocks
2. Computes stock metrics like mean-reversal

#### Build Status
<img src="https://travis-ci.com/wasimusu/trades.svg?branch=master" width="100">

### Platform
* Linux (Xenial/Ubuntu 18.04)
* Python 3.5, 3.7

### Project TODOs
- Store list of stocks observed by users
- Get quote for a stock (Start price, end price, volume, average volume)
- Store k days of stock data for each ticker
    - Do not download same data again. Or. Do not lose data
- Send email/message once the stock reaches a BUY or SELL
- *OPTIONAL*
- Get google trends data
- Get the sentiment regarding particular ticker