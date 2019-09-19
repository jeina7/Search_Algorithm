def move(node, direction):
    blank_index = node.status.index(0)
    new_state = copy.deepcopy(node.status)

    if direction == 'up':
        if blank_index not in [0, 1, 2]:
            move_num = new_state[blank_index-3]
            new_state[blank_index] = move_num
            new_state[blank_index-3] = 0
            return Node(new_state, node.depth+1, 'up', 0, node)
        else:
            return None

    elif direction == 'down':
        if blank_index not in [6, 7, 8]:
            move_num = new_state[blank_index+3]
            new_state[blank_index] = move_num
            new_state[blank_index+3] = 0
            return Node(new_state, node.depth+1, 'down', 0, node)
        else:
            return None

    elif direction == 'right':
        if blank_index not in [2, 5, 8]:
            move_num = new_state[blank_index+1]
            new_state[blank_index] = move_num
            new_state[blank_index+1] = 0
            return Node(new_state, node.depth+1, 'right', 0, node)
        else:
            return None

    elif direction == 'left':
        if blank_index not in [0, 3, 6]:
            move_num = new_state[blank_index-1]
            new_state[blank_index] = move_num
            new_state[blank_index-1] = 0
            return Node(new_state, node.depth+1, 'left', 0, node)
        else:
            return None


def expand(node):
    expanded = []
    expanded.append(move(node, 'up'))
    expanded.append(move(node, 'left'))
    expanded.append(move(node, 'right'))
    expanded.append(move(node, 'down'))
    expanded = [i for i in expanded if i]
    return expanded


GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

def h1(node):
    # number of tiles out of place
    h = 0
    for status_num, goal_num in zip(node.status, GOAL_STATE):
        if status_num != goal_num:
            h += 1
    return h


def h2(node):
    # summation of manhattan distance to the place
    h = 0
    for status_idx, status_num in enumerate(node.status):
        goal_idx = GOAL_STATE.index(status_num)
        status_x, status_y = status_idx % 3, status_idx // 3
        goal_x, goal_y = goal_idx % 3, goal_idx // 3
        h += abs(status_x - goal_x) + abs(status_y - goal_y)
    return h


def get_path(start_node, goal_node):
    path = []
    current_node = goal_node
    while current_node.status != start_node.status:
        path.insert(0, current_node.direction)
        current_node = current_node.parent
    return path
