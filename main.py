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
    # const_matrix = matrix
    msg = str()
    ans = None
    if n != m:
        msg = "The determinant of the matrix can be found only in a square matrix."
    else:
        if len(matrix)==1:
            return int(matrix[0][0]), n == m, msg
        else:
            for i in range(0,n):
                ans = 0
            # for i in range(0,n+1):
            #     coefficient, no_answer, no_msg = det_coefficient(matrix, n,m, 1, int(i)+1)
            #     print(coefficient)
            #     # ans += int(matrix[0][int(i)]) * int(coefficient)
            #     ans += int(coefficient)
                coefficient, no_answer, no_msg = det_coefficient(matrix, n, m, 1, int(0) + 1)
                print(coefficient)
                #ans += int(matrix[0][int(i)]) * int(coefficient)
        return ans, n == m, msg


def det_coefficient(matrix_accepted, n, m, i, j): # Count coefficient
    #if len(matrix)==1:
    #    return matrix[0][0], 1, 1
    #else:
    #    return det(decrease_matrix(matrix, i-1, j-1), i, j)
    if len(matrix_accepted) == 1:
        return det(matrix_accepted, i, j)
    else:
        return det(decrease_matrix(matrix_accepted, i - 1, j - 1), n-1, m-1)


def decrease_matrix(old_matrix, i, j): # Decrease the matrix in order to count coefficient
    new_matrix = old_matrix
    for a in range(0, len(old_matrix)):
        del new_matrix[a][int(j)]
    del new_matrix[int(i)]
    return new_matrix


got_answer = False
while not got_answer:
    user_option = option()
    user_matrix, n, m = get_matrix()
    if user_option == 1:
        ans, got_answer, msg = det(user_matrix, n, m)
        if not msg:
            print("Answer:", ans)
        print(msg)
