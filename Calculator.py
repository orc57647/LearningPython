# Simple Calculator Program made by Owen Conrad 9/6/2022
from scipy.stats import binom
from cmath import sqrt

# Define our addition operand
def Add_Calc():
    a = float(input("Please input a value for the 1st number: "))
    b = float(input("Please input a value for the 2nd number: "))
    operand = a + b
    print(a, '+', b, '=', operand)

# Define our subtraction operand
def Minus_Calc():
    a = float(input("Please input a value for the 1st number: "))
    b = float(input("Please input a value for the 2nd number: "))
    operand = a - b
    print(a, '-', b, '=', operand)

# Define our subtraction operand
def Product_Calc():
    a = float(input("Please input a value for the 1st number: "))
    b = float(input("Please input a value for the 2nd number: "))
    operand = a * b
    print(a, '*', b, '=', operand)

# Define our subtraction operand
def Quotient_Calc():
    a = float(input("Please input a value for the 1st number: "))
    b = float(input("Please input a value for the 2nd number: "))
    operand = a / b
    print(a, '/', b, '=', operand)

def Quadratic_calc():
    print('\nHere is the base equation: Ax^2 + Bx + C')
    a = float(input("Please input a value for A: "))
    b = float(input("Please input a value for B: "))
    c = float(input("Please input a value for C: "))
    operand1 = ((-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a))
    operand2 = ((-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a))
    print('\nYour roots are', operand1, 'and', operand2)

# Define our Binomial Distribution operand
def Binomial_Calc():
    n = float(input("Please input a value for the number of trials: "))
    k = float(input("Please input a value for the number of successes desired: "))
    p = float(input("Please input a value for the probability of getting a success in one trial: "))
    operand = binom.pmf(n=n, k=k, p=p)
    print("The probability of", k, 'successes in', n, 'trials is', operand)

# Define our calculator
def Calculator():
    if Selection == 1:
        Add_Calc()
    elif Selection == 2:
        Minus_Calc()
    elif Selection == 3:
        Product_Calc()
    elif Selection == 4:
        Quotient_Calc()
    elif Selection == 5:
        Quadratic_calc()
    elif Selection == 6:
        Binomial_Calc()

while True:
    print('\nHello this is the calculator app')
    print('1 = Addition')
    print('2 = Subtraction')
    print('3 = Multiplication')
    print('4 = Division')
    print('5 = Quadratic Formula')
    print('6 = Binomial Distribution')
    Selection = float(input('\nPlease select from the operations above: '))
    Calculator()
    
    next_calc = input('\nWould you like to do another calculation? ')
    if next_calc == 'no' or next_calc == 'n':
        print('\nThank you for using the calculator app. Have a great day!')
        break