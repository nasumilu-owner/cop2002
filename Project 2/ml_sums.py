#!/usr/bin/env python3

# Michael Lucas
# COP2002.054
# 2020-1-12
# Project 2 - Sums of odd and even numbers

def main() : 
    print('Sum of odd and even numbers')
    print('=' * 40)

    try_again = 'y'
    while try_again.lower() == 'y' : 
        inputted_value = None
        while inputted_value is None or (inputted_value < 1 or inputted_value > 50):
            try:
                inputted_value = int(input('Your number must be between 1 and 50: '))
            except ValueError:
                print('Try agian.', end=' ')

        sum_range = range(1, inputted_value+1, 2)
        num_type = 'odd'
        if inputted_value % 2 == 0 :
            sum_range = range(2, inputted_value +1, 2)
            num_type = 'even'

        print(f'\nYour number is an {num_type} number.')

        total = 0
        for i in sum_range:
            total += i

        print(f'The sum of the {num_type} numbers from {sum_range.start} to {sum_range.stop - 1} is: {total}\n')
        try_again = input('\nTry again? (y/n)')

if __name__ == "__main__":
    main()