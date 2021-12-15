def set_initial_state(n):
    people_list = [(0, 0)] * n
    return 0, people_list


def get_final_state(n):
    people_final_list = [(1, 1)] * n
    return 1, people_final_list


def verify_final_state(state):
    if state == get_final_state(len(state[1])):
        print('Is final state')
    else:
        print('It is not a final state')


if __name__ == '__main__':
    state = set_initial_state(3)
    verify_final_state(state)

    print(state[1][2][0])

