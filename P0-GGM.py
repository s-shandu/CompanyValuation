#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 08:24:55 2024

@author: sshanducisco.com
"""

Net_Income  = 3867.59  # $219M
DividendsPaid = 1889.64  #107M
RoE = 0.1607 # Taken from Moneyweb
Ks = 0.106 # Calculated from CAPM
D1 = 388.52


def RetentioRatio(Net_Income, DividendsPaid):
    rr = (Net_Income - DividendsPaid)/Net_Income
    return rr
    
rr = RetentioRatio(Net_Income, DividendsPaid)
print("Retention Ratio(RR):",rr)

def GrowthRate(RoE,rr):
    g = RoE*rr
    return g

g = GrowthRate(RoE, rr)
print("GrowthRate:",g)

def ExpectedSharePrice(D1,Ks,g):
    P0 = (D1*g)/(Ks-g)
    return P0

P0 = ExpectedSharePrice(D1,Ks,g)
print ("ExpectedSharePrice:",P0)





    




