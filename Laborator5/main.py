from random import sample
import math


def get_available_balls(n, m):
    available_balls = []
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            available_balls.append(i)
    return available_balls


def get_initial_state(n, m, k):
    state = [0, get_random_seq(k, get_available_balls(n, m)), k]
    return state


def get_random_seq(k, available_balls):
    random_seq = sample(available_balls, k)
    return random_seq


def state_A(n, m, k):
    state = get_initial_state(n, m, k)
    return state


a_state = [1, 3, 3, 1]


def check_final_state(a_state, state, n, m, k):
    if state[1] == a_state[1] and state[0] < 2 * n:
        print('A castigat jucatorul B')
        return 1
    elif state[0] > 2 * n:
        print('A castigat jucatorul A')
        return 1


def check_state(a_state, state, n, m, k):
    count = 0
    for index in range(0, k):
        if state[1][index] == a_state[1][index]:
            count = count + 1
    state[2] = count
    return count


def get_score(a_state, list_of_color, n, m, k):
    count = 0
    for index in range(0, k):
        if a_state[index] == list_of_color[index]:
            count += 1
    return count


def validate_sequence(seq, n, m, k):
    if len(seq) != k:
        return 0
    for ball in seq:
        if seq.count(ball) > m:
            return 0
        if ball > n:
            return 0
    return 1


def read_seq(n, m, k):
    sequence = []
    print(f'Introdu o secventa de {k} culori din intervalul [1, {n}] unde o culoare se poate repeta de maxim {m} ori')
    for i in range(1, k + 1):
        number = int(input(f'Bila de pe pozitia {i} : '))
        sequence.append(number)
    if validate_sequence(sequence, n, m, k):
        return sequence
    print('Invalid')
    return 0


def game(n, m, k):
    sequence = []
    b_state = [0, [], 0]
    step = 1
    a_balls = get_initial_state(n, m, k)
    print(a_balls)
    play = 1
    while play:
        b_state[0] = step
        print(f'Pasul : {step}')
        sequence = read_seq(n, m, k)
        while sequence == 0:
            print('Secventa invalida')
            sequence = read_seq(n, m, k)
        b_state[1] = sequence
        check_state(a_balls, b_state, n, m, k)
        print(f'Secventa introdusa are {b_state[2]} bile exact ca in secventa de ghicit')
        print(b_state)
        step += 1
        if check_final_state(a_balls, b_state, n, m, k):
            play = 0
        if step > 2 * n:
            play = 0
            print('A castigat jucatorul A')


combinations = []
candidates = []


def createSet(n, m, k):
    current = [0 for _ in range(k)]
    elements = []
    for i in range(1, n + 1, 1):
        elements.append(i)
    createCombinations(k, 0, current, elements)


def createCombinations(combination_length, position, current, elements):
    if position == combination_length:
        combinations.append(current[:])
        return
    for j in range(len(elements)):
        current[position] = elements[j]
        createCombinations(combination_length, position + 1, current, elements)


def get_min(combinations: list) -> list:
    min_score = get_score(a_state, combinations[0], n, m, k)
    index_min = 0
    for combination in combinations:
        current_score = get_score(a_state, combination, n, m, k)
        if current_score < min_score:
            min_score = current_score
            index_min = combinations.index(combination)
    return combinations[index_min]


def min_max(step, n, m, k, current_state, known_positions, level, alpha, beta):
    if get_score(a_state, current_state, n, m, k) == k:
        print(current_state)
        return 1
    if step > 2 * (2 * n):
        return 0

    if step % 2:
        current_score = get_score(a_state, current_state, n, m, k)
        if current_score < beta:
            beta = current_score
            # min_max(step + 1, n, m, k, current_score, known_positions, level, alpha, beta)
        for candidate in combinations:
            if validate_sequence(candidate, n, m, k):
                score = get_score(a_state, candidate, n, m, k)
                # print(candidate, score)
                if score <= current_score:
                    combinations.remove(candidate)
        # print(combinations)
        level = level + 1
        next_state = get_min(combinations)
        min_max(step + 1, n, m, k, next_state, known_positions, level, alpha, beta)
    else:
        current_score = get_score(a_state, current_state, n, m, k)
        if current_score > alpha:
            alpha = current_score
        min_max(step + 1, n, m, k, current_state, known_positions, level, alpha, beta)


if __name__ == '__main__':
    n = 3
    m = 2
    k = 4
    color_list = [1, 1, 2, 2]
    createSet(n, m, k)
    min_max(0, n, m, k, color_list, 0, 0, -math.inf, math.inf)
