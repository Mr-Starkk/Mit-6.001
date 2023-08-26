# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 00:20:41 2023

@author: yashs
"""
#need to buy a house!
annual_salary = float(input("Enter your annual salary:"))
monthly_salary = annual_salary/12
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter The cost of your dream home :"))
portion_down_payment = 0.25 * total_cost
current_savings = 0
semi_annual_raise = float(input("Enter the semiannual raise, as a decimal:"))
#after every month I get a return of
#(current_savings * 0.04) / 12

monthly_returns = 0
months = 0

while current_savings < portion_down_payment : 
    
    current_savings += (portion_saved * monthly_salary) + (current_savings * 0.04 / 12)
    months += 1
    if months % 6 == 0:
        monthly_salary += semi_annual_raise * monthly_salary

print("Number of months:", months)