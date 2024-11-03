#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 12:14:37 2024

@author: sshanducisco.com
"""

dividend_per_share = 388.52  # Expected dividend per share next year (22USDc)
cost_of_equity = 0.106  # Required rate of return on equity (10.6%), calculated via CAPM
dividend_growth_rate = 0.082  # Expected constant dividend growth rate (8.2% calculated)

def gordon_growth_model(dividend_per_share, cost_of_equity, dividend_growth_rate):
    """
    Calculates the intrinsic value of a stock using the Gordon Growth Model (GGM).

    Args:
        dividend_per_share (float): The expected dividend per share for the next period.
        cost_of_equity (float): The required rate of return on equity.
        dividend_growth_rate (float): The expected constant growth rate of dividends.

    Returns:
        float: The intrinsic value of the stock.

    Raises:
        ValueError: If the cost of equity is less than or equal to the dividend growth rate.
    """

    if cost_of_equity <= dividend_growth_rate:
        raise ValueError("Cost of equity must be greater than dividend growth rate.")

    intrinsic_value = dividend_per_share / (cost_of_equity - dividend_growth_rate)
    return intrinsic_value

stock_value = gordon_growth_model(dividend_per_share, cost_of_equity, dividend_growth_rate)
print("Intrinsic value of the stock:", stock_value)