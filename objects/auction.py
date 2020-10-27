'''
Created on Oct. 26, 2020

@author: jbowles

Wrapper object for auctions for a site's ads

'''

class Auction(object):
    '''
    classdocs
    '''
    site = ""
    units = []
    bids = []

    def __init__(self, jsonObj):
        '''
        Constructor
        '''
        self.site = jsonObj["site"]
        self.units = jsonObj["units"]
        self.bids = jsonObj["bids"]