'''
Created on Oct. 26, 2020

@author: jbowles

Wrapper object for Bids from input.json, not used currently
'''

class Bid(object):
    '''
    classdocs
    '''
    bidder = ""
    bid = 0
    unit = ""
    adjustedBid = 0

    def __init__(self, jsonObj):
        '''
        Constructor
        '''
        self.bidder = jsonObj["bidder"]
        self.bid = jsonObj["bid"]
        self.unit = jsonObj["unit"]