from itertools import combinations


def set_initial_state(n):
    initial_state = [0] * ((2 * n) + 1)
    return initial_state


def get_final_state(n):
    final_state = [1] * ((2 * n) + 1)
    return final_state


def verify_final_state(state: list) -> bool:
    if state == get_final_state(len(state) // 2):
        print('Is final state')
        return True
    else:
        print('It is not a final state')
        return False


def generate_transition(state: list, *persons) -> list:
    ok = 0
    for person in persons:
        if state[0] == state[person]:
            state[person] = (state[person] + 1) % 2
            ok = 1
    if ok:
        state[0] = (state[0] + 1) % 2
    return state


def validate_state(state: list) -> bool:
    n = (len(state) - 1) // 2
    for woman in range(1, n + 1):
        if state[woman] != state[woman + n]:
            for man in range(n + 1, 2 * n + 1):
                if state[woman] == state[man] and man != woman + n:
                    return False
    return True


def generate_all_transition(state: list):
    n = (len(state) - 1) // 2
    state_saver = list(state)
    transition_list = []
    comb = combinations(range(1, 2 * n + 1), 2)
    for pair in list(comb):
        state = list(state_saver)
        i = int(pair[0])
        j = int(pair[1])
        # print(f'({i}, {j})')
        # print(state)
        transition_list.append(generate_transition(state, i, j))

    for i in range(1, 2 * n + 1):
        state = list(state_saver)
        transition_list.append(generate_transition(state, i))

    # for transition in transition_list:
    #     print(transition)

    return transition_list


all_passed_transitions = []
solution = []
queue = []


def backtraking(state: list):
    global solution
    n = (len(state) - 1) // 2
    if state == get_final_state(n):
        return True

    global all_passed_transitions
    all_passed_transitions.append(state)

    transitions = generate_all_transition(state)
    for transition in transitions:
        if validate_state(transition) and (transition not in all_passed_transitions):
            if backtraking(transition):
                solution.append(transition)
                return True
    all_passed_transitions.remove(state)
    return False


parents = []
solution_bfs = []


def bfs(state: list):
    global all_passed_transitions
    all_passed_transitions = []
    n = (len(state) - 1) // 2
    queue.append(state)
    parents.append(-1)
    all_passed_transitions.append(state)
    while queue:
        actual_state = queue.pop(0)
        # print(actual_state)
        transitions = generate_all_transition(actual_state)
        for transition in transitions:
            if validate_state(transition) and (transition not in all_passed_transitions):
                # print(transition)
                all_passed_transitions.append(transition)
                queue.append(transition)
                parents.append(all_passed_transitions.index(actual_state))
                if transition == get_final_state(n):
                    index = len(parents) - 1
                    # print(transition)
                    solution_bfs.append(transition)
                    while parents[index] != -1:
                        # print(all_passed_transitions[parents[index]])
                        solution_bfs.append(all_passed_transitions[parents[index]])
                        index = parents[index]
                    return


side = {
    0: "stang",
    1: "drept"
}


def get_heuristic_value(state: list):
    n = (len(state) - 1) // 2
    sum = 0
    for i in range(1, 2 * n + 1):
        if state[i] == 1:
            sum += 1
    return sum / (2 * n)


def hill_climbing(state: list):
    n = (len(state) - 1) // 2
    current_state = list(state)
    find_solution = 0
    best_n = 0
    while True:
        current_value = get_heuristic_value(current_state)
        neighbours = generate_all_transition(current_state)
        best_neighbour = list(current_state)
        print(current_state)

        for neighbour in neighbours:
            if validate_state(neighbour):
                n_value = get_heuristic_value(neighbour)
                if n_value > best_n:
                    best_n = n_value
                    best_neighbour = list(neighbour)
        if best_neighbour == current_state:
            break
        if best_n > current_value:
            for index in range(1, 2 * n + 1):
                if current_state[index] != best_neighbour[index]:
                    if 1 <= index <= n:
                        print(
                            f'Am mutat femeia {index} de pe malul {side[current_state[0]]} pe malul {side[best_neighbour[index]]}')
                    elif n < index <= 2 * n:
                        print(
                            f'Am mutat barbatul {index - n} de pe malul {side[current_state[0]]} pe malul {side[best_neighbour[index]]}')
            current_state = list(best_neighbour)
            current_value = best_n

        if current_state == get_final_state(n):
            find_solution = 1
            break

    if find_solution:
        print('Solutie')
    else:
        print('Nu se gaseste solutie')


queue_star = []
all_explored_states = []


def Sort_Tuple(tup):
    tup.sort(key=lambda x: x[1], reverse=True)
    return tup


distance = []


def A_star(state: list):
    n = (len(state) - 1) // 2
    current_state = list(state)

    best_score = get_heuristic_value(current_state)
    neighbours = generate_all_transition(current_state)
    level = 1
    for neighbour in neighbours:
        if validate_state(neighbour):
            queue_star.append([neighbour, get_heuristic_value(neighbour) + level])

    Sort_Tuple(queue_star)

    score = queue_star[0][1]
    current_state = queue_star.pop(0)[0]

    while current_state not in all_explored_states and score > best_score:
        if current_state == get_final_state(n):
            best_score = score
        all_explored_states.append(current_state)
        neighbours = generate_all_transition(current_state)
        level = level + 1
        # print(current_state)
        for neighbour in neighbours:
            if validate_state(neighbour):
                queue_star.append([neighbour, level + get_heuristic_value(neighbour)])
                if neighbour in all_explored_states:
                    all_explored_states.remove(neighbour)
        Sort_Tuple(queue_star)
        current_state = queue_star.pop(0)


if __name__ == '__main__':
    n = int(input('Please choose n : '))
    state = set_initial_state(n)

    alg = int(input('''Please choose the algorithm : 
    1. Backtracking
    2. BFS
    3. HillClimbing
    4. A* \n'''))

    if alg == 1:
        backtraking(state)
        print('-----BKT-----')
        print(state)
        solution.append(state)
        ant = list(state)
        for index in range(len(solution) - 2, -1, -1):
            for i in range(0, len(solution[index])):
                if ant[i] != solution[index][i]:
                    if 1 <= i <= n:
                        print(f'Am mutat femeia {i} de pe malul {side[ant[0]]} pe malul {side[solution[index][0]]}')
                    if 4 <= i <= 2 * n:
                        print(
                            f'Am mutat barbatul {i - n} de pe malul {side[ant[0]]} pe malul {side[solution[index][0]]}')
            print(solution[index])
            ant = list(solution[index])
    elif alg == 2:
        bfs(state)
        print('-----BFS-----')
        print(state)
        ant = list(state)
        for index in range(len(solution_bfs) - 2, -1, -1):
            for i in range(0, len(solution_bfs[index])):
                if ant[i] != solution_bfs[index][i]:
                    if 1 <= i <= n:
                        print(f'Am mutat femeia {i} de pe malul {side[ant[0]]} pe malul {side[solution_bfs[index][0]]}')
                    if 4 <= i <= 2 * n:
                        print(
                            f'Am mutat barbatul {i - n} de pe malul {side[ant[0]]} pe malul {side[solution_bfs[index][0]]}')
            print(solution_bfs[index])
            ant = list(solution_bfs[index])
    elif alg == 3:
        hill_climbing(state)
    elif alg == 4:
        A_star(state)
