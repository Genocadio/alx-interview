#!/usr/bin/python3
""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """ Rotate 2D Matrix 90 degrees
    """
    for x, y in enumerate(zip(*reversed(matrix))):
        matrix[x] = list(y)
