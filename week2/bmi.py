# bmi.py
# This program calculates your Body Mass Index (BMI).
# author: Barry Gardiner

height = int(input("Please Enter Your Height In Centimetres:"))
weight = int(input("Please Enter Your Weight in kilograms:"))

bmi = ((weight) / ((height/100))**2)#Formula: weight (kg) / [height (m)]2

print('Your BMI is {}'.format(round(bmi,2)))#Using format to fromat BMI