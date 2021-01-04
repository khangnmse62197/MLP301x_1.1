import pandas as pd
import numpy as np


def open_file(file_name):
    if not file_name.__contains__('.txt'):
        file_name += '.txt'
    try:
        with open(file_name, 'r') as file:
            print('Successfully opened ' + str(file_name))
            valid_lines = validate_format(file.read().split('\n'))
            print_statistics(valid_lines)
            save_grade(file_name, valid_lines)

    except IOError:
        print('File cannot be found.')


def print_statistics(valid_lines):
    valid_lines_values = np.array(list(valid_lines.values()))

    print('Mean (average) score: ' + str(np.mean(valid_lines_values)))
    print('Highest score: ' + str(np.max(valid_lines_values)))
    print('Lowest score: ' + str(np.min(valid_lines_values)))
    print('Range of scores: ' + str(np.max(valid_lines_values) - np.min(valid_lines_values)))
    print('Median score: ' + str(np.median(valid_lines_values)))


def save_grade(file_name, valid_lines):
    file_grade_name = file_name.replace('.txt', '_grade.txt')
    with open('output/' + file_grade_name, 'w+') as file:
        for key, value in valid_lines.items():
            file.writelines(key + ',' + str(value) + '\n')
    print('File saved: ' + file_grade_name)


def validate_format(file):
    print('**** ANALYZING ****')
    count_error_line = 0
    valid_lines = {}
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

        valid_lines.update(compute_grade(values))  # valid line
    if count_error_line == 0:
        print('No errors found!')

    print('**** REPORT ****')
    print('Total valid lines of data:' + str(len(valid_lines)))
    print('Total invalid lines of data:' + str(count_error_line))
    return valid_lines


def compute_grade(line):
    """
    calculate grade and return a dict with key = the student’s ID number, value = grade
        +4 points for every right answer
        0 points for every skipped answer
        -1 point for every incorrect answer
    """
    answer_key = 'B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D'.split(',')
    grade = 0
    for i in range(1, line.__len__()):  # skip the id
        if line[i] == '':
            grade += 0
        elif line[i] == answer_key[i - 1]:
            grade += 4
        else:
            grade -= 1
    return {line[0]: grade}


filename = input("Enter a class to grade (i.e. class1 for class1.txt): ")
open_file(filename)
is_continue = 'Y'
while is_continue == 'Y' or is_continue == 'y':
    is_continue = input("Continue[y/N]: ")
    if is_continue == 'y' or is_continue == 'Y':
        filename = input("Enter a class to grade (i.e. class1 for class1.txt): ")
        open_file(filename)
    else:
        print('Bye!')
        is_continue = 'N'
