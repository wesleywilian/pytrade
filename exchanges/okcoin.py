#!/usr/bin/python

import urllib.request
import json


# lastbid, lastask [price, volume]

def update(pair):
    global asks, bids, lastbid, lastask;
    if pair == 0:
        url = "https://www.okcoin.com/api/v1/depth.do?symbol=btc_usd"
    elif pair == 1:
        url = "https://www.okcoin.com/api/v1/depth.do?symbol=ltc_usd"
    elif pair == 2:
        url = "https://www.okcoin.com/api/v1/depth.do?symbol=eth_usd"
    elif pair == 3:
        url = "https://www.okcoin.com/api/v1/depth.do?symbol=bch_usd"
    request = urllib.request.urlopen(url).read().decode("utf-8")
    data = json.loads(request);
    asks = data["asks"];
    bids = data["bids"];
    lastask = (float(asks[-1][0]), asks[-1][1])
    lastbid = (float(bids[0][0]), bids[0][1])
