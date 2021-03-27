#!/usr/bin/env python3

# Michael Lucas
# COP2002.054
# 2020-1-12
# Project 5  - Cessna 172N Time and Fuel Calculator

from math import floor, ceil

def get_distance():
    """Gets a valid distance value in nauticla miles
    
    Return:
        float: User inputed distance value as nautical miles

    """
    distance = None
    while distance is None:
        try:
            distance = float(input('\nDistance in nautical miles: '))
        except ValueError:
            print('Try again!', end=' ')
    return distance


def flight_time(distance):
    """Calculates the flight time in minutes based for a given `distance`.
    
    Parameters:
        distance:float The flight distance in nautical miles

    Return:
        float: The flight time in minutes @ 120 nautical miles per hour
    """
    return distance * 60 / 120


def flight_fuel(flight_time):
    """Calculates the fuel need for a flight based upon a given amount of
    `flight_time`. An additional 30 minutes is added as a safety buffer.
    
    Parameters: 
        flight_time:float The flight time in minutes
    
    Return:
        float: The amount of fuel needed rounded up to one decimal place. 
    """
    fuel = ((flight_time + 30)/60) * 8.4
    return ceil(fuel * 10)/10


def main():
    """
    1. Prints the programs title
    2. Enter main loop while calculate == 'y'
        a. Gets the user inputted distance
        b. Calculates the fligth time in minutes
        c. Calculates the fuel needed for minutes of flight time
        d. Prints the flight time and required fuel
        d. Asked if the user wishes to calculate the fuel for another flight
        e. Goto Step 1
    3. Terminate
    """
    print('Aircraft Fuel Calculator')
    calculate = 'y'
    while calculate.lower() == 'y':
        distance = get_distance()
        time = flight_time(distance) # minutes
        fuel = flight_fuel(time) # gallons
        #used the floor function from math rather. For at least one could have used the // operator
        print(f'Flight time: {floor(time/60)} hour(s) and {floor(time % 60)} minute(s)')
        print(f'Required fuel: {fuel} gallons \n')
        calculate = input('Continue? (y/n): ')


if __name__ == "__main__":
    main()