class Node:

    def __init__(self, status, depth, direction=None, cost=0, parent=None):
        self.status = status
        self.depth = depth
        self.direction = direction
        self.cost = cost
        self.parent = parent


    def show_map(self):
        for idx, i in enumerate(self.status):
            if (idx+1) % 3 == 0:
                print(i)
            else:
                print('{:3}'.format(str(i)), end='')
        print('')
