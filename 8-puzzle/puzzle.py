import copy
from .utils import move, expand, h1, h2, get_path
from .node import Node


GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

class Puzzle:

    def __init__(self, puzzle_array):
        self.START_NODE = Node(puzzle_array, 0)


    def __DFS(self, verbose=False):
        visited = []
        max_depth = 0
        max_stack_len = 0
        stack = [self.START_NODE, ]
        while stack:
            node = stack.pop()
            if node.status not in visited:
                visited.append(node.status)
                if node.status == GOAL_STATE:
                    break
                stack.extend([i for i in self.expand(node) if i not in visited])
                max_stack_len = max(max_stack_len, len(stack))
                max_depth = max(max_depth, node.depth)

                if verbose:
                    print('depth:', node.depth)
                    print('visited list:', visited, '(visited len: {})'.format(len(visited)))
                    print('stack:', stack, '(len: {})'.format(len(stack)))

                if len(visited) >= 100000:
                    print('search space exceeded.')
                    break

        return self.START_NODE, len(visited), max_stack_len, max_depth


    def __BFS(self, verbose=False):
        visited = []
        max_depth = 0
        max_queue_len = 0
        queue = [self.START_NODE, ]
        while queue:
            node = queue.pop(0)
            if node.status not in visited:
                visited.append(node.status)
                if node.status == GOAL_STATE:
                    break
                queue.extend([i for i in self.expand(node) if i not in visited])
                max_queue_len = max(max_queue_len, len(queue))
                max_depth = max(max_depth, node.depth)

                if verbose:
                    print('depth:', node.depth)
                    print('visited list:', visited, '(visited len: {})'.format(len(visited)))
                    print('queue:', queue, '(len: {})'.format(len(queue)))

                if len(visited) >= 100000:
                    print('search space exceeded.')
                    break

        return self.START_NODE, len(visited), max_queue_len, max_depth


    def __Astar(self, h_func, verbose=False):
        if h_func == 'h1':
            h_func = h1
        elif h_func == 'h2':
            h_func = h2

        open_, closed_ = [], []
        max_open_len = 0
        max_depth = 0

        start_node = copy.deepcopy(self.START_NODE)
        start_node.cost = 0 + h_func(self.START_NODE)
        open_.append(start_node)

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
                goal_node = v
                return start_node, goal_node, len(closed_), max_open_len, max_depth

            closed_.append(v)
            children = [i for i in self.expand(v)]
            for i in children:
                i.cost = i.depth + h_func(i)
            open_.extend(children)
            max_open_len = max(max_open_len, len(open_))

            open_ = sorted(open_, key=lambda i: i.cost)
            closed_ = sorted(closed_, key=lambda i: i.cost)


    def show_result(self, algorithm, h_func=None):
        if algorithm == "dfs":
            start_node, closed_len, max_len, max_depth = self.__DFS()
        elif algorithm == "bfs":
            start_node, closed_len, max_len, max_depth = self.__BFS()
        elif algorithm == "astar":
            start_node, goal_node, closed_len, max_len, max_depth = self.__Astar(h_func)

        print('start node:', start_node.status)
        if algorithm == 'astar':
            print('path:', self.get_path(start_node, goal_node))
        print('visited node:', visited_len)
        print('max queue length:', max_queue_len)
        print('max depth:', max_depth)
