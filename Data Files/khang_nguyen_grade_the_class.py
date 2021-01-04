import pandas as pd
import numpy as np


def open_file(file_name):
    if not file_name.__contains__('.txt'):
        file_name += '.txt'
    try:
        with open(file_name, 'r') as file:
            print('Successfully opened ' + str(file_name))
            validate_format(file.read().split('\n'))
    except IOError:
        print('File cannot be found.')


def validate_format(file):
    print('**** ANALYZING ****')
    count_lines = len(file)
    count_error_line = 0
    for line in file:
        values = line.split(',')
        if len(values) != 26:
            print('[ERROR1] Invalid line of data: does not contain exactly 26 values: ')
            print(line)
            count_error_line += 1
            continue

        first_value = values[0].split('N')
        if first_value[0] != '':
            print('[ERROR2]  N# is invalid. It should contain the character “N” at beginning ')
            print(line)
            count_error_line += 1
            continue

        if len(first_value) > 2:
            print('[ERROR3]  N# is invalid. It should contain only 1 character “N” at beginning:')
            print(line)
            count_error_line += 1
            continue

        if len(first_value[1]) != 8:
            print('[ERROR4]  N# is invalid. Need 8 numeric after N ')
            print(line)
            count_error_line += 1
            continue

        try:
            int(first_value[1])
        except ValueError:
            count_error_line += 1
            print('[ERROR5]  N# is invalid. It should contain 8 numeric characters. ')
            print(line)

            continue
    if count_error_line == 0:
        print('No errors found!')

    print('**** REPORT ****')
    print('Total valid lines of data:' + str(count_lines - count_error_line))
    print('Total invalid lines of data:' + str(count_error_line))


filename = input("Enter a filename: ")
open_file(filename)
is_continue = 'Y'
while is_continue == 'Y' or is_continue == 'y':
    is_continue = input("Continue[y/N]: ")
    if is_continue == 'y' or is_continue == 'Y':
        filename = input("Enter a filename: ")
        open_file(filename)
    else:
        print('Bye!')
        is_continue = 'N'
