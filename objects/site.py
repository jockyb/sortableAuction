'''
Created on Oct. 26, 2020

@author: jbowles

Wrapper object for valid sites from config.json  
'''

class Site(object):
    '''
    classdocs
    '''
    name = ""
    #maybe make a bidder object
    bidders = []
    floor = 0


    #input json object from array of "sites" in config.json 
    def __init__(self, jsonObj):
        '''
        Constructor
        '''
        self.name = jsonObj["name"]
        self.bidders = jsonObj["bidders"] 
        self.floor =jsonObj["floor"]