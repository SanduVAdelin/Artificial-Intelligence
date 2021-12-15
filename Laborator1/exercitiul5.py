from typing import List


def spiral_matrix(matrix : List[List]) -> None:
    string = ""
    matrix_dim = len(matrix)
    visited = [[False]*matrix_dim
               for _ in range(matrix_dim)
               ]
    i = j = 0
    turn = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for _ in range(matrix_dim ** 2):
        print(_)
        string += matrix[i][j]
        visited[i][j] = True
        new_i, new_j = i + di[turn], j + dj[turn]
        if new_i in range(matrix_dim) and new_j in range(matrix_dim) and not visited[new_i][new_j]:
            i = new_i
            j = new_j
        else:
            turn = (turn + 1) % 4
            i += di[turn]
            j += dj[turn]
    print(f'Result : {string}')


if __name__ == '__main__':
    spiral_matrix([
         ['f', 'i', 'r', 's'],
         ['n', '_', 'l', 't'],
         ['o', 'b', 'a', '_'],
         ['h', 't', 'y', 'p']
     ])