import random


def init_q_table(rows, cols, actions):
    q = dict()
    for i in range(0, rows):
        for j in range(0, cols):
            q[(i, j)] = dict()
            for action in actions:
                q[(i, j)][action] = random.uniform(0, 1)
    return q


def init_state():
    initial_state = (0, 0)
    return initial_state


def final_state():
    finals = [(1, 1), (1, 3), (2, 3), (3, 0), (3, 3)]
    return finals


def table_init(rows, cols):
    table = []
    for i in range(0, rows):
        row = []
        for j in range(0, cols):
            if i == rows - 1 and j == cols - 1:
                row.append(1)
            else:
                row.append(0)
        table.append(row)
    return table


def do_action(state: tuple[int, int], action: str):
    new_state = ()
    if action == 'N':
        new_state = (state[0] - 1, state[1])
    elif action == 'S':
        new_state = (state[0] + 1, state[1])
    elif action == 'E':
        new_state = (state[0], state[1] + 1)
    elif action == 'V':
        new_state = (state[0], state[1] - 1)
    return new_state


episodes = 1000000
learning_rate = 0.01
aux_fac = 0.99

if __name__ == '__main__':
    q = init_q_table(4, 4, ['N', 'S', 'E', 'V'])
    print(q[(0, 0)])
    print(q)
    print(table_init(4, 4))
