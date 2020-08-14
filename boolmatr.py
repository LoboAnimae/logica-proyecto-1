import numpy as np
from numpy.linalg import matrix_power
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
    pwr = 0
    for vert in range(2, vertices+1):
        pwr = matrix_power(temp, vert)
        temp2 = (temp2 | pwr)
    
    for vert in range(vertices):
        for sub in range(vertices):
            temp2[vert][sub] = 1 if int(temp2[vert][sub]) != 0 else 0
    return temp2



graph = [[0, 0, 1, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]
vertices = 4
print(boolmatrixprocedure(graph, vertices))
