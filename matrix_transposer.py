

def matrix_transposer(matrix01):

    matrix01_trans = []

    for i in range(len(matrix01[0])):
        new_row = []
        for j in range(len(matrix01)):
            new_row.append(matrix01[j][i])
        matrix01_trans.append(new_row)

    if matrix01 == matrix01_trans:
        return True
    else:
        return False


m = [[1,4,3],
     [2,6,5],
     [3,5,8]]

print(matrix_transposer(m))
