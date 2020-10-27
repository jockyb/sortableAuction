'''
Created on Oct. 26, 2020

@author: jbowles
'''
import sys
import json

#local imports
from objects import bidder
from objects import bid
from objects import site
from objects import auction

if __name__ == '__main__':
    
    confBidderDict = {}
    confSitesDict = {}
    
    inputAuctionList = []
    
    outputList = []
    
    #print(sys.argv[1])
    
    #TODO STDin sys.argv
    #with open(sys.argv[1]) as inputFile:
    #with open('input.json') as inputFile:
    #    inputData = json.load(inputFile)
    inputData = json.load(sys.stdin)

    #TODO make relative for docker
    with open('/auction/config.json') as configFile:
        configData = json.load(configFile)

    #print(configData)
    
    #Create input/config objects
    
    
    
    #TODO tie sites from auction to config

    
    for confBidder in configData["bidders"]:
        #print(confBidder["name"])
        thisBidder = bidder.Bidder(confBidder)
        confBidderDict[thisBidder.name]= thisBidder
    
    for confSite in configData["sites"]:
        #print(confBidder["name"])
        thisConfsite = site.Site(confSite)
        #confSitesList.append()
        confSitesDict[thisConfsite.name] = thisConfsite
    
    #For each auction, you should find the highest valid bidder for each ad unit, after applying the adjustment factor
    for inputAuction in  inputData:
        
        thisAuction = auction.Auction(inputAuction)
        inputAuctionList.append(thisAuction)
        
        #Dict with key = ad type, value = bid object, reset for each auction object
        winningBids = {}

        #Check if input site is a valid site from config
        if thisAuction.site in confSitesDict.keys():
            
            #Get auction floor for this site
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
    
            #remove adjustedBid and wrapper categories
            #TODO reorder for output
            for adType in winningBids:
                winningBids[adType].pop("adjustedBid")
            
            outputList.append(list(winningBids.values()))
    
    # Write output
    
    #TODO EMPTY LISTS
    
    
    
    #with open('output.json', 'w') as json_file:
    #    json.dump(outputList, json_file, indent = 4)
    print(json.dumps(outputList, indent = 4))
    
    
    #for x in inputAuctionList:
    #    print(x.site)
    #pass

    #TODO check all values types for money



