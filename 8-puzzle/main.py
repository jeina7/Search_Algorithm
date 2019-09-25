import argparse
from puzzle import Puzzle
from puzzle_solver import *

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('algorithm')
    parser.add_argument('initial_state')
    args = parser.parse_args()

    if args.algorithm.startswith('astar'):
        algorithm, h_func = args.algorithm.split("_")
    else:
        algorithm, h_func = args.algorithm, None

    puzzle_solver = Puzzle_Solver(args.initial_state)
    puzzle_solver.show_result(algorithm, h_func)


if __name__ == '__main__':
    main()
