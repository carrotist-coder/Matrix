from copy import deepcopy

MIN_NUMBER = -2147483648
MAX_NUMBER = 2147483647
options = {
    1: "Find the determinant of the matrix\n"
}


def get_input(msg, quantity, interval):
    # Get input from user: msg - message to show, quantity of the accepted parameters that are included in the interval
    good_ans_condition = False
    while not good_ans_condition:
        ans = list(input(msg).split())
        good_ans_condition = (len(ans) == quantity or quantity == -1)  # -1 means unlimited quantity of the parameters
        try:
            for element in ans:
                if not (int(element) in interval):
                    good_ans_condition = False
                    break
        except:
            good_ans_condition = False
        if good_ans_condition:
            if quantity == 1:
                ans = int(ans[0])
            return ans
        else:
            print("Something went wrong...")


def get_option():  # Print all the options and get user's response
    print("Options: \n", options)
    return get_input("Enter: ", 1, range(1, len(options) + 1))


class Matrix:
    def __init__(self):
        # Create the Matrix size n*m:
        self.matrix, self.n, self.m = self.get_matrix()

    def init_matrix(self, lines):  # Initialization the matrix from the keyboard
        matrix = []
        columns = -1
        for i in range(1, lines + 1):
            line = get_input("Line " + str(i) + ": ", columns, range(MIN_NUMBER, MAX_NUMBER + 1))
            if i == 1:
                columns = len(line)
            matrix.append(line)
        return matrix, lines, columns

    def get_matrix(self):  # Find out the number of lines in the matrix n*m.
        self.matrix, n, m = self.init_matrix(
            get_input("Enter the number of lines of the matrix n (1-99): ", 1, range(1, 100)))
        return self.matrix, n, m

    def det(self, matrix, n, m):  # Count determinant
        if n != m:
            print("The determinant of the matrix can be found only in a square matrix.")
            return None
        elif n == 1:
            return int(matrix[0][0])
        else:
            ans = 0
            const_matrix = deepcopy(matrix)
            for j in range(0, m):
                element = int(const_matrix[0][int(j)])
                coefficient = self.det_coefficient(matrix, n, m, 1, int(j) + 1)
                ans += element * int(coefficient) * (-1) ** (j % 2)
            return ans

    def det_coefficient(self, matrix_accepted, n, m, i, j):  # Count coefficients (algebraic additions)
        return self.det(self.decrease_matrix(matrix_accepted, i - 1, j - 1), n - 1, m - 1)

    def decrease_matrix(self, old_matrix, i, j):
        # Decrease the matrix an order of magnitude lower in order to count coefficient
        new_matrix = deepcopy(old_matrix)
        for a in range(0, len(old_matrix)):
            del new_matrix[a][int(j)]
        del new_matrix[int(i)]
        return new_matrix


got_answer = False
while not got_answer:
    user_option = get_option()
    user_matrix = Matrix()
    if user_option == 1:
        ans = user_matrix.det(user_matrix.matrix, user_matrix.n, user_matrix.m)
        if ans is not None:
            got_answer = True
        print("Answer:", user_matrix.det(user_matrix.matrix, user_matrix.n, user_matrix.m))
