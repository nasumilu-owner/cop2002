#!/usr/bin/env python3

# -----------------------------------------------------------------
# Michael Lucas
# COP2002.054
# 2020-1-15
# -----------------------------------------------------------------
# Description:
# -----------------------------------------------------------------
# Project 6  - Create a program that calculates the interest on a 
# loan. This program should make it easy for the user to enter 
# numbers
# -----------------------------------------------------------------

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
import locale

def main():
    """ 
    Application controller, i.e. main function. 
    
    1. Prompt user for loan amount (Line# 37)
        a. Normalize & validate
    2. Prompt user for interest rate (Line# 38)
        a. Normalize & validate
    3. Calculate interest rate (Line# 39)
    4. Output results (Lines# 41 - 45)
    5. Prompt to repeat 1 - 4 (Line# 46)
    """
    locale.setlocale(locale.LC_MONETARY, 'en_US')
    print('Welcome to the Interest Calculator')
    calcualte_interest = 'y'
    while calcualte_interest == 'y':
        loan_amount = prompt_loan_amount()
        interest_rate = prompt_interest_rate()
        interest_amount = loan_amount * interest_rate

        print('-' * 50)
        print(f'Loan Amount:      {locale.currency(loan_amount, grouping=True):>15}') #15 characters wide; right justified;
        print(f'Interest Rate:    {interest_rate:>15.3%}') #15 characters wide; right justified; % format to 3 decimal places
        print(f'Interest Amount:  {locale.currency(interest_amount, grouping=True):>15}') #15 characters wide; right justified;
        print('-' * 50)
        calcualte_interest = input('\nContinue? (y/n): ')


def prompt_loan_amount():
    """
    Prompts the user to input loan amount.
    
    The inputed value is normalizes and validates by calling the
    `normalize_loan_amount` function. Valid input is returned as an instance
    of Decimal.
    """
    loan_amount = normalize_loan_amount(input('\nEnter loan amount: '))
    while loan_amount is None:
        loan_amount = normalize_loan_amount(input('Invalid input! Enter loan amount:'))
    return loan_amount


def prompt_interest_rate():
    """
    Prompts user to input interest rate.
    
    The inputted value is normalizes and validates by calling the 
    `normalize_interest_rate` function. Valid input is returned as an instance
    of Decimal.
    """
    interest_rate = normalize_interest_rate(input('Enter interest rate: '))
    while interest_rate is None :
        interest_rate = normalize_interest_rate(input('Invalid input! Enter interest rate: '))
    return interest_rate

def normalize_interest_rate(value):
    """ 
    Intersest rate normalizer
    
    Expects the `value` to be a string. When a '%' symbol is 
    present the it will be replaced with an empty string.
    The value is returned as decimal format (e.g. 2.75% || 2.75 = 0.0275)

    Returns an instance of Decimal when valid; Otherwise `None`
    """
    if '%' in value:
        value = value.replace('%', '')

    try :   
        return Decimal(value)/100
    except: InvalidOperation

    return None

def normalize_loan_amount(value):
    """ 
    Loan amount normalizer
    
    Expects the `value` to be a string. When a cace insensitive 'k'
    is present the it will be replaced with '000'. When the 'k' is 
    found the normalizer will also replace any '.' with an empty string.
    (e.g. 12k = 12000 or 12.5K = 125000).  
    Lastly, all none numeric or '.' characters are replace with an 
    empty string. (e.g. $100,000 = 100000 or $1.25K = 125000)

    Returns an instance of Decimal when valid; Otherwise `None`
    """
    normalized_value = value.lower()
    if 'k' in normalized_value:
        normalized_value = normalized_value.replace('k', '000')
        normalized_value = normalized_value.replace('.', '')

    normalized_value = normalized_value.replace('$', '')
    normalized_value = normalized_value.replace(',', '')

    try: 
        return Decimal(normalized_value)
    except: InvalidOperation
    
    return None

if __name__ == "__main__":
    main()