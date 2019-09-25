import copy
from utils import move, expand, h1, h2, get_path, show_path
from puzzle import Puzzle


GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

class Puzzle_Solver:

    def __init__(self, initial_state):
        initial_state = initial_state.split(",")
        initial_state = [int(i) for i in initial_state]

        self.START_PUZZLE = Puzzle(initial_state, 0)


    def __DFS(self, verbose=False):
        visited = []
        max_depth = 0
        max_stack_len = 0
        stack = [self.START_PUZZLE, ]
        while stack:
            v = stack.pop()
            if v.status not in visited:
                visited.append(v.status)
                if v.status == GOAL_STATE:
                    break
                stack.extend([i for i in expand(v) if i not in visited])
                max_stack_len = max(max_stack_len, len(stack))
                max_depth = max(max_depth, v.depth)

                if verbose:
                    print('depth:', v.depth)
                    print('visited list:', visited, '(visited len: {})'.format(len(visited)))
                    print('stack:', stack, '(len: {})'.format(len(stack)))

                if len(visited) >= 100000:
                    print('search space exceeded.')
                    break

        goal_puzzle = v
        return self.START_PUZZLE, goal_puzzle, len(visited), max_stack_len, max_depth


    def __BFS(self, verbose=False):
        visited = []
        max_depth = 0
        max_queue_len = 0
        queue = [self.START_PUZZLE, ]
        while queue:
            v = queue.pop(0)
            if v.status not in visited:
                visited.append(v.status)
                if v.status == GOAL_STATE:
                    break
                queue.extend([i for i in expand(v) if i not in visited])
                max_queue_len = max(max_queue_len, len(queue))
                max_depth = max(max_depth, v.depth)

                if verbose:
                    print('depth:', v.depth)
                    print('visited list:', visited, '(visited len: {})'.format(len(visited)))
                    print('queue:', queue, '(len: {})'.format(len(queue)))

                if len(visited) >= 100000:
                    print('search space exceeded.')
                    break

        goal_puzzle = v
        return self.START_PUZZLE, goal_puzzle, len(visited), max_queue_len, max_depth


    def __Astar(self, h_func, verbose=False):
        if h_func == 'h1':
            h_func = h1
        elif h_func == 'h2':
            h_func = h2

        open_, closed_ = [], []
        max_open_len = 0
        max_depth = 0

        start_puzzle = copy.deepcopy(self.START_PUZZLE)
        start_puzzle.cost = 0 + h_func(self.START_PUZZLE)
        open_.append(start_puzzle)

        while True:
            if not open_:
                print('There is no solution.')
                return None

            while True:
                v = open_.pop(0) # lowest cost
                max_depth = max(max_depth, v.depth)

                if verbose:
                    print(v.status, v.cost)

                if closed_:
                    if v.status not in [i.status for i in closed_]:
                        break
                    else:
                        for i in closed_:
                            if v.status == i.status:
                                if v.cost <= i.cost:
                                    closed_.remove(i)
                                break
                else:
                    break

            if v.status == GOAL_STATE:
                goal_puzzle = v
                return start_puzzle, goal_puzzle, len(closed_), max_open_len, max_depth

            closed_.append(v)
            children = [i for i in expand(v)]
            for i in children:
                i.cost = i.depth + h_func(i)
            open_.extend(children)
            max_open_len = max(max_open_len, len(open_))

            open_ = sorted(open_, key=lambda i: i.cost)
            closed_ = sorted(closed_, key=lambda i: i.cost)


    def show_result(self, algorithm, h_func=None):
        if algorithm == "dfs":
            start_puzzle, goal_puzzle, closed_len, max_len, max_depth = self.__DFS()
        elif algorithm == "bfs":
            start_puzzle, goal_puzzle, closed_len, max_len, max_depth = self.__BFS()
        elif algorithm == "astar":
            start_puzzle, goal_puzzle, closed_len, max_len, max_depth = self.__Astar(h_func)

        print('start puzzle:', start_puzzle.status)
        if algorithm in ['astar', 'bfs']:
            print('path:', get_path(start_puzzle, goal_puzzle))
        print('visited nodes:', closed_len)
        print('max stack length:', max_len)
        print('max depth:', max_depth)
        show_path(start_puzzle, goal_puzzle)
