'''
Created on Oct. 26, 2020

@author: jbowles

Wrapper object for valid bidders from config.json

'''

class Bidder(object):
    '''
    classdocs
    '''
    name = ""
    adjustment = 0


    def __init__(self, jsonObj):
        '''
        Constructor
        '''
        self.name = jsonObj["name"]
        self.adjustment = jsonObj["adjustment"]
        