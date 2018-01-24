#!/usr/bin/python

import urllib.request
import json


def update(pair):
    global asks, bids, lastbid, lastask;
    if pair == 0:
        url = "https://api.kraken.com/0/public/Depth?pair=XBTUSD&count=10"; alias = "XXBTZUSD"
    elif pair == 1:
        url = "https://api.kraken.com/0/public/Depth?pair=LTCUSD&count=10"; alias = "XLTCZUSD"
    elif pair == 2:
        url = "https://api.kraken.com/0/public/Depth?pair=ETHUSD&count=10"; alias = "XETHZUSD"
    elif pair == 3:
        url = "https://api.kraken.com/0/public/Depth?pair=BCHUSD&count=10"; alias = "BCHUSD"
    request = urllib.request.urlopen(url).read().decode("utf-8")
    data = json.loads(request);
    asks = data["result"][alias]["asks"];
    bids = data["result"][alias]["bids"];
    lastask = (float(asks[0][0]), asks[0][1])
    lastbid = (float(bids[0][0]), bids[0][1])
