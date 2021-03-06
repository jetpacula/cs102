
import pathlib
import time
import typing as tp
import random 
import multiprocessing

import random
from typing import List, Optional, Set, Tuple




def run_solve(filename: str) -> None:
    grid = read_sudoku(filename)
    start = time.time()
    solve(grid)
    end = time.time()
    print(f"{filename}: {end-start}")

def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:

def read_sudoku(filename: str) -> List[List[str]]:

    """ Прочитать Судоку из указанного файла """
    digits = [c for c in open(filename).read() if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: List[List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: List[str], n: int) -> List[List[str]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов

    

    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """


    return [[i for i in values[start:start+n]] for start in range(len(values)) if start % n ==0]


    lenght = len(values)
    finish = []
    for i in range(0, lenght - 1, n):
        finish.append(values[i : i + n])
    return finish



def get_row(grid: List[List[str]], pos: Tuple[int, int]) -> List[str]:
    """Возвращает все значения для номера строки, указанной в pos

    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """


    return grid[pos[0]]


    return grid[pos[0]]

def get_col(grid: List[List[str]], pos: Tuple[int, int]) -> List[str]:
    """Возвращает все значения для номера столбца, указанного в pos

    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """


    return [row[pos[1]] for row in grid ]

    finish = []
    for i in range(len(grid)):
        finish.append(grid[i][pos[1]])
    return finish



def get_block(grid: List[List[str]], pos: Tuple[int, int]) -> List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos

    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """

    shiftx = pos[0]//3 #0
    shifty = pos[1]//3 #0
    res = []
    [[res.append(i) for i in row[shifty*3:3+shifty*3]]   for row in grid[shiftx*3:3+shiftx*3]]
    return res




    row = 3 * (pos[0] // 3)
    col = 3 * (pos[1] // 3)
    finish = []
    for i in range(3):
        for j in range(3):
            finish.append(grid[row + i][col + j])
    return finish



def find_empty_positions(grid: List[List[str]]) -> Optional[Tuple[int, int]]:
    """Найти первую свободную позицию в пазле

    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """

    for rownum, row in enumerate(grid):
        for colnum, col in enumerate(row):
            if col=='.':
                return (rownum, colnum)

    for first in range(len(grid)):
        for second in range(len(grid)):
            if grid[first][second] == ".":
                return (first, second)
    return None



def find_possible_values(grid: List[List[str]], pos: Tuple[int, int]) -> Set[str]:
    """Вернуть множество возможных значения для указанной позиции

    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """

    vals = set(get_col(grid,pos)+get_row(grid,pos)+get_block(grid,pos))
    return  {i for i in '123456789' if i not in vals}

    possible_numbers = set("123456789")
    row_numbers = set(get_row(grid, pos))
    col_numbers = set(get_col(grid, pos))
    block_numbers = set(get_block(grid, pos))
    result = possible_numbers - row_numbers - col_numbers - block_numbers
    return result



def solve(grid: List[List[str]]) -> Optional[List[List[str]]]:
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла

    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """

    


    pos = find_empty_positions(grid)
    if not pos:
        return grid
    row, col = pos

    for val in find_possible_values(grid,pos):
        grid[row][col] = val
        res = solve(grid)
        if res:
            return res
    grid[row][col] = '.'

               
def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """
    # TODO: Add doctests with bad puzzles
    for rownum, row in enumerate(solution):
        for colnum, col in enumerate(row):
            if solution[rownum][colnum] == '.':
                return False
            row_vals = get_row(solution,(rownum,colnum))
            col_vals = get_col(solution,(rownum,colnum))
            block_vals = get_block(solution,(rownum,colnum))


            if (len(set(row_vals)) < len( row_vals)) or ( len( set(col_vals)) < len(col_vals)) or( len( set(block_vals)) < len( block_vals)):
                return False
    return True




    for i in find_possible_values(grid, pos):
        grid[row][col] = i
        mean = solve(grid)
        if mean:
            return mean
    grid[row][col] = "."
    return None


def check_solution(solution: List[List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """
    # TODO: Add doctests with bad puzzles

    for row in range(len(solution)):
        result = set(get_row(solution, (row, 0)))
        if result != set("123456789"):
            return False

    for col in range(len(solution)):
        result = set(get_col(solution, (0, col)))
        if result != set("123456789"):
            return False

    for row in range(0, (len(solution) - 1), 3):
        for col in range(0, (len(solution) - 1), 3):
            result = set(get_block(solution, (row, col)))
            if result != set("123456789"):
                return False

    return True



def generate_sudoku(N: int) -> List[List[str]]:
    """Генерация судоку заполненного на N элементов

    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """

    grid = solve([["."] * 9 for _ in range(9)])
    N = 81 - min(81, N)
    while N:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if grid is not None:
            if grid[row][col] != ".":
                grid[row][col] = "."
                N -= 1
    return grid  # type: ignore


    grid = solve([["."] * 9 for _ in range(9)])
    N = 81 - min(81, N)
    while N:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if grid is not None:
            if grid[row][col] != ".":
                grid[row][col] = "."
                N -= 1
    return grid  # type: ignore

if __name__ == "__main__":
    for filename in ("puzzle1.txt", "puzzle2.txt", "puzzle3.txt"):
        p = multiprocessing.Process(target=run_solve, args=(filename,))
        p.start()

