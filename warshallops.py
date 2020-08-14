def warshall(array: list, vertices: int):
    """Calculates the closing matrix using the Warshall algorithm as described in the PDF.

    Args:
        array (list): Boolean matrix
        vertices (int): How many vertices there are in the boolean matrix mxn. m = n

    Returns:
        List of Lists: Before using numpy, a list had to be generated instead. This returns a list of lists. 
    """
    temp = [sub[:] for sub in array]
    for ini in range(vertices):
        for sub in range(vertices):
            for sec in range(vertices):
                temp[sub][sec] = temp[sub][sec] or (
                    temp[sub][ini] and temp[ini][sec])
    return temp


graph = [[0, 0, 1, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]
vertices = 4
for x in warshall(graph, vertices):
    print(x)
