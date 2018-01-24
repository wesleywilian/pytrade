#!/usr/bin/python

import urllib.request
import json


def update(pair):
    global asks, bids, lastbid, lastask
    if pair == 0:
        url = "https://poloniex.com/public?command=returnOrderBook&currencyPair=USDT_BTC&depth=10"
    elif pair == 1:
        url = "https://poloniex.com/public?command=returnOrderBook&currencyPair=USDT_LTC&depth=10"
    elif pair == 2:
        url = "https://poloniex.com/public?command=returnOrderBook&currencyPair=USDT_ETH&depth=10"
    elif pair == 3:
        url = "https://poloniex.com/public?command=returnOrderBook&currencyPair=USDT_BCH&depth=10"
    request = urllib.request.urlopen(url).read().decode("utf-8")
    data = json.loads(request);
    asks = data["asks"];
    bids = data["bids"];
    lastask = (float(asks[0][0]), asks[0][1])
    lastbid = (float(bids[0][0]), bids[0][1])
