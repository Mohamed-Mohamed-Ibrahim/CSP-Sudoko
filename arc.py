from asyncio import Queue
from collections import deque
from utils import *
sudoku_csp = None
arcs = None


def ac3():
    
    queue = deque(arcs)
    log_buffer = []
    valid = True

    log_buffer.append('Before ARC Domains:')

    for r in range(9):
        for c in range(9):
            log_buffer.append(f"{(r, c)}: {sudoku_csp['domains'][(r, c)]}")
    
    while len(queue) != 0:

        (Xi, Xj) = queue.popleft()
        
        if revise(Xi, Xj):
            if len(sudoku_csp['domains'][Xi]) == 0:
                valid = False
                break
            for xi, xj in arcs:
                if xj == Xi and (xi, Xi) not in queue:
                    queue.append((xi, Xi))


        

    log_buffer.append('After ARC Domains:')

    for r in range(9):
        for c in range(9):
            log_buffer.append(f"{(r, c)}: {sudoku_csp['domains'][(r, c)]}")

    with open('log.txt', 'w') as f:
        f.write('\n'.join(log_buffer))

    log_buffer.clear()

    return valid


def revise(Xi, Xj):
    # return True
    revised = False
    for x in str(sudoku_csp['domains'][Xi]):
        if not any((x, y) for y in str(sudoku_csp['domains'][Xj]) if  int(x) != int(y)):
            sudoku_csp['domains'][Xi] = str(sudoku_csp['domains'][Xi]).replace(x, '')
            revised = True
    return revised


def print_tree():
    pass


if __name__ == "__main__":

    # Example Sudoku puzzle (0 represents an empty cell)
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    sudoku_csp = create_sudoku_csp(puzzle)

    arcs = define_sudoku_arcs()
    print(ac3())
    check=3
    for r in range(check):
        for c in range(check):
            print(sudoku_csp['domains'][(r, c)])
    

