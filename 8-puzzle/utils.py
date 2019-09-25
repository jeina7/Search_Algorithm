import copy
from puzzle import Puzzle

def move(puzzle, direction):
    blank_index = puzzle.status.index(0)
    new_state = copy.deepcopy(puzzle.status)

    if direction == 'up':
        if blank_index not in [0, 1, 2]:
            move_num = new_state[blank_index-3]
            new_state[blank_index] = move_num
            new_state[blank_index-3] = 0
            return Puzzle(new_state, puzzle.depth+1, 'up', 0, puzzle)
        else:
            return None

    elif direction == 'down':
        if blank_index not in [6, 7, 8]:
            move_num = new_state[blank_index+3]
            new_state[blank_index] = move_num
            new_state[blank_index+3] = 0
            return Puzzle(new_state, puzzle.depth+1, 'down', 0, puzzle)
        else:
            return None

    elif direction == 'right':
        if blank_index not in [2, 5, 8]:
            move_num = new_state[blank_index+1]
            new_state[blank_index] = move_num
            new_state[blank_index+1] = 0
            return Puzzle(new_state, puzzle.depth+1, 'right', 0, puzzle)
        else:
            return None

    elif direction == 'left':
        if blank_index not in [0, 3, 6]:
            move_num = new_state[blank_index-1]
            new_state[blank_index] = move_num
            new_state[blank_index-1] = 0
            return Puzzle(new_state, puzzle.depth+1, 'left', 0, puzzle)
        else:
            return None


def expand(puzzle):
    expanded = []
    expanded.append(move(puzzle, 'up'))
    expanded.append(move(puzzle, 'left'))
    expanded.append(move(puzzle, 'right'))
    expanded.append(move(puzzle, 'down'))
    expanded = [i for i in expanded if i]
    return expanded


GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

def h1(puzzle):
    # number of tiles out of place
    h = 0
    for status_num, goal_num in zip(puzzle.status, GOAL_STATE):
        if status_num != goal_num:
            h += 1
    return h


def h2(puzzle):
    # summation of manhattan distance to the place
    h = 0
    for status_idx, status_num in enumerate(puzzle.status):
        goal_idx = GOAL_STATE.index(status_num)
        status_x, status_y = status_idx % 3, status_idx // 3
        goal_x, goal_y = goal_idx % 3, goal_idx // 3
        h += abs(status_x - goal_x) + abs(status_y - goal_y)
    return h


def get_path(start_puzzle, goal_puzzle):
    path = []
    current_puzzle = goal_puzzle
    while current_puzzle.status != start_puzzle.status:
        path.insert(0, current_puzzle.direction)
        current_puzzle = current_puzzle.parent
    return path


def show_path(start_puzzle, goal_puzzle):
    path = []
    current_puzzle = goal_puzzle
    while current_puzzle.status != start_puzzle.status:
        path.insert(0, current_puzzle)
        current_puzzle = current_puzzle.parent
    path.insert(0, start_puzzle)
    print("\n0 START!")
    for idx, i in enumerate(path):
        if i.direction:
            print("{}".format(idx), i.direction)
        i.show_map()
    print("GOAL!!")
    return path
