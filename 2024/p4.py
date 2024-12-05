#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic
from collections import defaultdict
from itertools import chain
from more_itertools import transpose

testdata_a = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

testdata_b = """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
"""

def groups(data, func):
    grouping = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y])):
            grouping[func(x, y)].append(data[y][x])
    return list(map(grouping.get, sorted(grouping)))

def countseq(lst, seq):
    count = 0
    seq_len = len(seq)
    for i in range(len(lst) - seq_len + 1):
        if lst[i:i + seq_len] == seq:
            count += 1
    return count

def check_submatrix(submatrix):
    """
    Valid submatrices are one of four rotations of:
    M.S -> M.M -> S.M -> S.S
    .A. -> .A. -> .A. -> .A.
    M.S -> S.S -> S.M -> M.M
    """
    for _ in range(4):
        submatrix = [list(row) for row in zip(*submatrix[::-1])]
        if  submatrix[0][0] == 'M' \
        and submatrix[0][2] == 'S' \
        and submatrix[1][1] == 'A' \
        and submatrix[2][0] == 'M' \
        and submatrix[2][2] == 'S':
            return True
    return False

def solveA(data):
    matrix = [[char for char in row] for row in data.splitlines()]
    cols  = list(filter(lambda t: len(t) >= 4, groups(matrix, lambda x, y: x)))
    rows  = list(filter(lambda t: len(t) >= 4, groups(matrix, lambda x, y: y)))
    fdiag = list(filter(lambda t: len(t) >= 4, groups(matrix, lambda x, y: x + y)))
    bdiag = list(filter(lambda t: len(t) >= 4, groups(matrix, lambda x, y: x - y)))

    count = 0
    for lst in chain(cols, rows, fdiag, bdiag):
        count += countseq(lst, ['X','M','A','S'])
        count += countseq(lst, ['S','A','M','X'])
    
    return count

def solveB(data):
    matrix = [[char for char in row] for row in data.splitlines()]
    submatrices = [[row[c:c+3] for row in matrix[r:r+3]] for r in range(len(matrix)-2) for c in range(len(matrix[0])-2)]
    count = 0
    for sm in submatrices:
        if check_submatrix(sm): count += 1
    return count
        
if __name__ == "__main__":
    assert solveA(testdata_a) == 18
    submit(solveA(data), part='a')

    assert solveB(testdata_b) == 9
    submit(solveB(data), part='b')