import numpy as np


def boolmatrixprocedure(array, vertices):
    """Proceeds to calculare the closure matrix using the simple Bool Matrix algorithm as described in the PDF

    Args:
        array (list): Array to be used. Only 1's and 0's allowed.
        vertices ([type]): How many vertices the matrix has. This is because in this mxn matrix, m = n

    Returns:
        Numpy Obj: Array that has been closured
    """
    temp = np.array(array)
    temp2 = np.array(array)
    i = 2
    for k in range(vertices):
        temp = temp.dot(temp)
        for i in range(vertices):
            for j in range(vertices):
                temp2[i][j] = temp2[i][j] or temp[i][j]
                temp2[i][j] = 1 if temp2[i][j] != 0 else 0
    return temp2


# graph = [[0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
#          [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
#          [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
#          [0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
#          [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#          [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [1, 1, 1, 0, 1, 0, 1, 0, 0, 0],
#          [0, 1, 0, 1, 1, 0, 0, 0, 1, 0],
#          [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]
# vertices = 10

# print(boolmatrixprocedure(graph, vertices))
