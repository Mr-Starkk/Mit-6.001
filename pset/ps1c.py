# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 00:20:53 2023

@author: yashs
"""
#need to buy a house!
annual_salary = float(input("Enter the starting salary:"))
monthly_salary = round(annual_salary/12,4)
months = 36
total_cost = 1000000
portion_down_payment = 0.25 * total_cost
current_savings = 0
semi_annual_raise = 0.07
epsilon = 100
low = 0.0      #lowest savings rate
high = 1.0     # highest savings rate
savings_rate = (low + high)/2

#after every month I get a return of
#(current_savings * 0.04) / 12
counter = 0 #steps in bisection search

while abs(current_savings - portion_down_payment) >= epsilon and savings_rate < 0.995 : 
    
    #reinitialise variables to their starting state
    current_savings = 0
    monthly_salary = round(annual_salary/12,4)
    savings_rate = round((low + high)/2,4)
    
    counter += 1
    
    for i in range(months+1) : 
        
        current_savings += round(savings_rate * monthly_salary,4) + round(current_savings * 0.04 / 12,4)
        if i % 6 == 0 and i != 0:
            monthly_salary += round(semi_annual_raise * monthly_salary,4)
            
    if current_savings > portion_down_payment:
        high = savings_rate
    if current_savings < portion_down_payment:
        low = savings_rate
    
if savings_rate >= 0.995:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate:", savings_rate)
print("Steps in bisection search:", counter)
