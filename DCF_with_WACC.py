#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 13:58:23 2024

@author: sshanducisco.com
"""
# DCF Analysis with WACC

# Assuming the following parameters:
risk_free_rate = 0.03  # 3% risk-free rate
market_risk_premium = 0.07  # 7% market risk premium
beta = 1.2  # Stock's beta
cost_of_debt = 0.05  # 5% cost of debt
tax_rate = 0.28  # 28% tax rate
debt_to_equity_ratio = 0.29  # Debt-to-equity ratio (Debt = 2239, Equity = 7789)
free_cash_flows = [1049.54, 1135.60, 1228.72, 1329.48,1438.49]  # Projected free cash flows
terminal_value = 1556.45  # Estimated terminal value

def capital_asset_pricing_model(risk_free_rate, market_risk_premium, beta):
    """
    Calculates the cost of equity using CAPM.

    Args:
        risk_free_rate (float): Risk-free rate of return.
        market_risk_premium (float): Market risk premium.
        beta (float): Stock's beta.

    Returns:
        float: Cost of equity.
    """

    cost_of_equity = risk_free_rate + beta * market_risk_premium
    return cost_of_equity

def weighted_average_cost_of_capital(cost_of_equity, cost_of_debt, tax_rate, debt_to_equity_ratio):
    """
    Calculates the weighted average cost of capital (WACC).

    Args:
        cost_of_equity (float): Cost of equity.
        cost_of_debt (float): Cost of debt.
        tax_rate (float): Corporate tax rate.
        debt_to_equity_ratio (float): Debt-to-equity ratio.

    Returns:
        float: WACC.
    """

    weight_of_equity = 1 / (1 + debt_to_equity_ratio)
    weight_of_debt = debt_to_equity_ratio / (1 + debt_to_equity_ratio)

    wacc = (weight_of_equity * cost_of_equity) + (weight_of_debt * cost_of_debt * (1 - tax_rate))
    return wacc

def discounted_cash_flow_model(free_cash_flows, discount_rate, terminal_value=None):
    """
    Calculates the intrinsic value using DCF.

    Args:
        free_cash_flows (list): List of projected free cash flows.
        discount_rate (float): Discount rate (WACC).
        terminal_value (float, optional): Terminal value. Defaults to None.

    Returns:
        float: Intrinsic value.
    """

    present_value_of_cash_flows = sum(
        cash_flow / (1 + discount_rate)**period
        for period, cash_flow in enumerate(free_cash_flows, 1)
    )

    if terminal_value:
        present_value_of_terminal_value = terminal_value / (1 + discount_rate)**len(free_cash_flows)
        present_value_of_cash_flows += present_value_of_terminal_value

    return present_value_of_cash_flows


# Calculate cost of equity using CAPM
cost_of_equity = capital_asset_pricing_model(risk_free_rate, market_risk_premium, beta)

# Calculate WACC
wacc = weighted_average_cost_of_capital(cost_of_equity, cost_of_debt, tax_rate, debt_to_equity_ratio)

# Calculate intrinsic value using DCF
intrinsic_value = discounted_cash_flow_model(free_cash_flows, wacc, terminal_value)

print("WACC:", wacc)
print("Intrinsic value of the stock:", intrinsic_value)