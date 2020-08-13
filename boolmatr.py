import numpy as np

def boolmatrixprocedure(array, vertices):
    temp = np.array(array)
    temp2 = np.array(array)
    i = 2
    for k in range(vertices):
        temp = temp.dot(temp)
        for i in range(vertices):
            for j in range(vertices):
                temp2[i][j] = temp2[i][j] or temp[i][j]
    return temp2




# graph = [[0, 0, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1], [1, 0, 1, 0]]
# vertices = 4

# print(boolmatrixprocedure(graph, vertices))

