
import bs4
import requests
import xml
from bs4 import BeautifulSoup

def parsePrice():
    r = requests.get('https://finance.yahoo.com/quote/DOGE-USD?p=DOGE-USD')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    price = soup.find('div', {'class':'D(ib) smartphone_Mb(10px) W(70%) W(100%)--mobp smartphone_Mt(6px)'}).find('span').text
    return price

"""
    Variables of initial buy prices
    Used to calculate gains and losses of those individual buys

    Buy History:
    jan28 $140.34 at $0.046116
    jan28 $300.22 at $0.077376
    feb3 $99.97 at $0.034189
    average cost $0.054893
"""
currentDogeValue = 0
floatedBoughtAtList = []
floatedBuyList = []
updatedDogeValue = -1
initialBuyList = [140.34, 300.22, 99.97]
initialInvestment = 0
overallAverageCost = 0.054893
priceBoughtAtList = [0.046116, 0.077376, 0.034189]


for item in initialBuyList:
    floatedBuyList.append(float(initialBuyList[item]))

for item2 in initialInvestment:
    floatedBoughtAtList.append(float(priceBoughtAtList[item2]))

for i in initialBuyList:
    initialInvestment = float(initialInvestment) + floatedBuyList[i]




while True:

    absoluteValue = 0
    difference = 0
    percentDifference = 0
    moneyEndAmount = 0
    updatedDogeValue = int(parsePrice())



    if(currentDogeValue != updatedDogeValue):
        currentDogeValue = updatedDogeValue
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("CURRENT DOGE PRICE: "+currentDogeValue)
        for i in floatedBuyList:
            print("For initial buy value: "+initialBuyList[i])
            difference = priceBoughtAtList[i] - updatedDogeValue
            percentDifference = difference/priceBoughtAtList[i] * 100
            print("Percent Difference: %"+percentDifference)
            if(difference > 0):
                moneyEndAmount = floatedBuyList[i] + (floatedBuyList[i] * abs(difference/priceBoughtAtList[i]))
            if(difference < 0):
                moneyEndAmount = floatedBuyList[i] - (floatedBuyList[i] * abs(difference/priceBoughtAtList[i]))
            print("Gains/Loss: "+moneyEndAmount)
        