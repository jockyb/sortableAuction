'''
Created on Oct. 26, 2020

@author: jbowles

Module to accomplish task set forth in 
https://github.com/sortable/auction-challenge

The program should then load the input (JSON) from standard input that contains a list of auctions to run.
Each auction lists the site, which ad units are being bid on, and a list of bids that have been requested on your behalf.

The output of your program should be a JSON list of auction results printed to stdout. The result of each auction is a list of winning bids.
The contents of output.json are an example of valid output. Ensure that when run as above, the only output of your program on stdout is the auction results.


'''
import sys
import json

#local imports
from objects import bidder
# Didn't end up using this structure
#from objects import bid
from objects import site
from objects import auction

if __name__ == '__main__':
    
    confBidderDict = {}
    confSitesDict = {}
    
    # To be used if auctions need a second pass or the be referenced after
    #inputAuctionList = []
    
    outputList = []
    
    #Load input file from stdin
    #TODO add file validation and error reporting, not currently in project scope
    #DEBUG use local file for debugging
    #with open('input.json') as inputFile:
    #    inputData = json.load(inputFile)
    inputData = json.load(sys.stdin)

    #Load config file containing valid bidders and sites
    #TODO make independent of docker config
    with open('/auction/config.json') as configFile:
        configData = json.load(configFile)
    
    #Add configs list of bidders and sites in dict to reference by site/bidder name
    for confBidder in configData["bidders"]:
        #print(confBidder["name"])
        thisBidder = bidder.Bidder(confBidder)
        confBidderDict[thisBidder.name]= thisBidder
    
    for confSite in configData["sites"]:
        #print(confBidder["name"])
        thisConfsite = site.Site(confSite)
        confSitesDict[thisConfsite.name] = thisConfsite
    
    #For each auction, you should find the highest valid bidder for each ad unit, after applying the adjustment factor
    for inputAuction in  inputData:
        
        thisAuction = auction.Auction(inputAuction)
        #inputAuctionList.append(thisAuction)
        
        #Dict with key = ad type, value = bid object, reset for each auction object
        winningBids = {}

        #Check if input site is a valid site from config
        if thisAuction.site in confSitesDict.keys():
            
            #Get auction floor value for this site, don't consider bid valid if below this once adjusted
            auctionFloor = confSitesDict[thisAuction.site].floor

            for acutionBid in thisAuction.bids:
    
                #check if bidder is valid
                if acutionBid["bidder"] in confBidderDict.keys() and acutionBid["unit"] in thisAuction.units :
                    # Get adjustment factor for bidder and update bid value
                    adjustedlValue = acutionBid["bid"] * (1 + confBidderDict.get(acutionBid["bidder"]).adjustment)
                    acutionBid["adjustedBid"] = adjustedlValue
                    #print(adjustedlValue)
                    
                    #replace current winning bid if higher and more than floor value
                    if (acutionBid["unit"] not in winningBids or adjustedlValue > winningBids[acutionBid["unit"]]["adjustedBid"]) and adjustedlValue>= auctionFloor:
                        #print("new winner")
                        winningBids[acutionBid["unit"]] = acutionBid
                    
                else:
                    #TODO add fail state or reporting of invalid bidder
                    #print("invalid bidder: " + acutionBid["bidder"])
                    pass
    
            #remove adjustedBid and wrapper categories for output
            for adType in winningBids:
                winningBids[adType].pop("adjustedBid")
            
            outputList.append(list(winningBids.values()))
    
    # Write output
    # Write to file if debugging
    # TODO add debug run mode
    #with open('output.json', 'w') as json_file:
    #    json.dump(outputList, json_file, indent = 4)
    print(json.dumps(outputList, indent = 4))
    
    pass

    #TODO check all values types for money and rounding issues 



