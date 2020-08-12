def warshall(array, vertices): 
        temp =[sub[:] for sub in array] 
        for ini in range(vertices): 
            for sub in range(vertices): 
                for sec in range(vertices): 
                    temp[sub][sec] = temp[sub][sec] or (temp[sub][ini] and temp[ini][sec]) 
        return temp
    