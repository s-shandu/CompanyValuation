#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 08:48:55 2024

@author: sshanducisco.com

"""

# Calculating AGA PE Ratio, with data from Moneyweb Website
P0 = 49036.00 # quoted in cents
EPS = 4.75

def calculate_pe_ratio(current_stock_price, earnings_per_share):
    pe_ratio = (current_stock_price / earnings_per_share)/1000
    return pe_ratio

current_stock_price = P0
earnings_per_share = EPS

pe_ratio = calculate_pe_ratio(current_stock_price, earnings_per_share)
print("P/E Ratio:", pe_ratio)