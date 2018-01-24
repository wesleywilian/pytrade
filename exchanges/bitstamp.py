#!/usr/bin/python

import urllib.request
import json


def update(pair):
    global asks, bids, lastbid, lastask
    if pair == 0:
        url = "https://www.bitstamp.net/api/v2/order_book/btcusd/"
    elif pair == 1:
        url = "https://www.bitstamp.net/api/v2/order_book/ltcusd/"
    elif pair == 2:
        url = "https://www.bitstamp.net/api/v2/order_book/ethusd/"
    elif pair == 3:
        url = "https://www.bitstamp.net/api/v2/order_book/bchusd/"
    request = urllib.request.urlopen(url).read().decode("utf-8")
    data = json.loads(request);
    asks = data["asks"];
    bids = data["bids"];
    lastask = (float(asks[0][0]), asks[0][1])
    lastbid = (float(bids[0][0]), bids[0][1])
