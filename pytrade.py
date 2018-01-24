#!/usr/bin/python3.5

import sys
sys.path.append('exchanges')
import poloniex
import kraken
import bitstamp
import okcoin
import time
import threading

coin = ["Bitcoin", "Litecoin", "Ethereum", "Bitcoin Cash"]
coin_index = 0
coin_index_max = len(coin) - 1
index = [["Poloniex", poloniex, [0, 1, 2, 3]], ["Kraken", kraken, [0, 1, 2, 3]], ["Bitstamp", bitstamp, [0, 1, 2, 3]],
         ["OKCoin", okcoin, [0, 1, 2, 3]]]

while True:
    if coin_index > coin_index_max:    coin_index = 0
    thread = []
    time.sleep(2)

    for exchange in index:
        print('[UPDATING] {}'.format(exchange[0]))
        thread.append(threading.Thread(target=exchange[1].update(coin_index)))
        thread[-1].start()
    for c in range(0, len(index)):
        thread[c].join()

    for exchange in index:
        for exchange2 in index:
            if exchange[1] != exchange2[1] and coin_index in exchange[2] and coin_index in exchange2[2]:
                if exchange[1].lastask[0] - exchange2[1].lastbid[0] < 0:
                    print(
                        '[TRADE] Buy {} on\t{}   \tat {:.8f}\tthen Sell on {}\tat {:.8f}\tProfits of {:.8f} ({:.4f}%)'.format(
                            coin[coin_index], exchange[0], exchange[1].lastask[0], exchange2[0],
                            exchange2[1].lastbid[0],
                            exchange2[1].lastbid[0] - exchange[1].lastask[0],
                            exchange2[1].lastbid[0] / exchange[1].lastask[0]))
                elif exchange[1].lastbid[0] - exchange2[1].lastask[0] > 0:
                    print(
                        '[TRADE] Sell {} on\t{}   \tat {:.8f}\tthen Buy on {}\tat {:.8f}\tProfits of {:.8f} ({:.4f}%)'.format(
                            coin[coin_index], exchange[0], exchange[1].lastbid[0], exchange2[0],
                            exchange2[1].lastask[0],
                            exchange[1].lastbid[0] - exchange2[1].lastask[0],
                            exchange[1].lastbid[0] / exchange2[1].lastask[0]))
    coin_index = coin_index + 1
