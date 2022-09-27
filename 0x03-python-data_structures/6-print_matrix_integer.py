#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for b in range(len(matrix)):
        for h in range(len(matrix[b])):
            print("{:d}".format(matrix[b][h]), end='')
            if h != len(matrix[b]) - 1:
                print(' ', end='')
        print()
