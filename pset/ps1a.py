# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 00:20:09 2023

@author: yashs
"""
#need to buy a house!
annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter The cost of your dream home :"))
portion_down_payment = 0.25 * total_cost
current_savings = 0

#after every month I get a return of
#(current_savings * 0.04) / 12

monthly_returns = 0
months = 0

while current_savings < portion_down_payment : 
    months += 1
    monthly_returns = ((portion_saved * annual_salary)/12) + ((current_savings * 0.04) / 12)
    current_savings = current_savings + monthly_returns

print("Number of months:", months)