#!/usr/bin/env python3

# Michael Lucas
# COP2002.054
# 2020-1-12
# Project 1 - Area and Perimeter
# This program uses input from the user to calucalte 
# the area and permimter of a rectangle.

def main() :
    name = input('Please enter your name: ')
    print('\nThe Area and Perimeter Program')
    length = float(input('\nPlease enter the length: '))
    width = float(input('Please enter the width: '))

    # f-string method
    print(f'\nArea = {length * width}')
    print(f'Perimeter = {(2 * width) + (2 * length)}')
    print(f'{name}, thank you for using this program!')

    #string concatenation method
    #print('\nArea = ' + str(length * width))
    #print('Perimeter = ' + str((2 * width) + (2 * length)))
    #print(name + ', thank you for using this program!')


if __name__ == "__main__":
    main()
