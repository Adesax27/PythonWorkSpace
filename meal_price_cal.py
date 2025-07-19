#!/usr/bin/env python
# coding: utf-8

#### Project: Meal Price Calculator

child_meal = float(input("what the price of childs meal? "))
adult_meal = float(input("what the price of adult meal? "))
childNum = int(input("Number of children are? "))
adultNum = int(input("The number of adults are? "))

# adding values for subtotal
mul_child_meal = (childNum) * (child_meal)

mul_adult_meal = (adultNum) * (adult_meal)

subtotal = (mul_child_meal) + (mul_adult_meal)
print(f" Subtotal: ${subtotal}")

#Getting subtotal
sub = (mul_adult_meal + mul_child_meal)
print(f"The subtotal of children and adult meals is ${sub}")

# input for sales tax
sales_tax = float(input("Please enter sales tax rate? "))

SalesTax = (sub * sales_tax)/ 100
print(f"Sales Tax: ${SalesTax}")

#adding subtotal and sales tax
Total = (subtotal + SalesTax)
print(f" Total: ${Total}")

#asking payment amount
payment = float(input("please enter your payment amount? "))
print(payment)

change = float(payment - Total)
print(f" Your change is ${change:.2f}.")
