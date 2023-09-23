MIN_NUMBER = -2147483648
MAX_NUMBER = 2147483647


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
    for i in range(1,lines+1):
        line = get_input("Line " + str(i) + ": ", columns, range(MIN_NUMBER, MAX_NUMBER))
        if i==1:
            columns = len(line)
        matrix.append(line)
    return matrix, lines, columns


matrix, n, m = init_matrix(get_input("Enter the number of lines of the matrix n (1-99): ", 1, range(1, 99)))

