#!/usr/bin/env python3

# Michael Lucas
# COP2002.054
# 2020-1-12
# Project 3  - Real Estate Values


def main():
    print('\tReal Estate Values')
    print('*' * 35)
    home_values = get_values()
    if len(home_values) != 0 :
        print('*' * 35)
        print('Prices of homes in your area:') 
        print(home_values)
        print('*' * 35)
        print(f'The median value is $ {median_value(home_values)}')
        print(f'The average sale price is $ {average_value(home_values)}')
        print(f'The minimum sale price is $ {min(home_values)}')
        print(f'The maximum sale price is $ {max(home_values)}')
    else : 
        print('No home values were inputed, thank you!')


def average_value(values):
    '''Calculates the average value from an array of values.'''
    return sum(values)/len(values)


def median_value(values):
    '''Calculates the median value from an array of values.'''
    length = len(values)
    #median value for odd number of values inputted
    if(length % 2 == 1):
        return values[ int((length + 1)/2) - 1 ]
    #median value for even number of values inputted
    return (values[ int((length/2) - 1) ] + values[int((length/2))]) / 2


def get_values():
    '''Gets an array of home prices from standard input.'''
    values = []
    value = get_value()
    while value != -99 :
        values.append(value)
        value = get_value()

    values.sort()
    return values

def get_value():
    '''Gets a valid home value'''
    value = None
    while value is None:
        try:
            value = float(input('Enter cost of one home or -99 to quit: '))
        except ValueError:
            print('Try again!', end=' ')
    
    return value



if __name__ == "__main__":
    main()