from copy import deepcopy
MIN_NUMBER = -2147483648
MAX_NUMBER = 2147483647
options = [
    "1. Find the determinant of the matrix\n"
]


def get_input(msg, quantity, interval):
    condition = False
    while not condition:
        ans = list(input(msg).split())
        condition = (len(ans) == quantity or quantity == -1)
        try:
            for element in ans:
                if not (int(element) in interval):
                    condition = False
                    break
        except:
            condition = False
        if condition:
            if quantity == 1:
                ans = int(ans[0])
            return ans
        else:
            print("Something went wrong...")


def init_matrix(lines):
    matrix = []
    columns = -1
    for i in range(1, lines + 1):
        line = get_input("Line " + str(i) + ": ", columns, range(MIN_NUMBER, MAX_NUMBER + 1))
        if i == 1:
            columns = len(line)
        matrix.append(line)
    return matrix, lines, columns


def option():
    print("Options: \n", options)
    return get_input("Enter: ", 1, range(1, len(options) + 1))


def get_matrix():
    matrix, n, m = init_matrix(get_input("Enter the number of lines of the matrix n (1-99): ", 1, range(1, 99)))
    return matrix, n, m


def det(matrix, n, m):  # Count determinant
    if n != m:
        print("The determinant of the matrix can be found only in a square matrix.")
        return None
    elif n == 1:
        return int(matrix[0][0])
    else:
        ans = 0
        const_matrix = deepcopy(matrix)
        for i in range(0, n):
            for j in range(0, m):
                element = int(const_matrix[int(i)][int(j)])
                matrix = deepcopy(const_matrix)
                coefficient = det_coefficient(matrix, n, m, int(i)+1, int(j) + 1)
                ans += element * int(coefficient)
        return ans


def det_coefficient(matrix_accepted, n, m, i, j):  # Count coefficient
    return det(decrease_matrix(matrix_accepted, i - 1, j - 1), n - 1, m - 1)


def decrease_matrix(old_matrix, i, j):  # Decrease the matrix in order to count coefficient
    new_matrix = deepcopy(old_matrix)
    for a in range(0, len(old_matrix)):
        del new_matrix[a][int(j)]
    del new_matrix[int(i)]
    return new_matrix


got_answer = False
while not got_answer:
    user_option = option()
    user_matrix, n, m = get_matrix()
    if user_option == 1:
        print("Answer:", det(user_matrix, n, m))