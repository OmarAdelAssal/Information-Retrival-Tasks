import numpy as np

def edit_distance(s1, s2):
    # n for rows , m for columns
    n, m = len(s1), len(s2)
    matrix = np.zeros((n + 1, m + 1), dtype=int)

    # loop for rows
    for i in range(1, n + 1):
        matrix[i][0] = i
    # loop for columns
    for j in range(1, m + 1):
        matrix[0][j] = j
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                # take the diagonal because it is the minimum value
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + 1)
                
    print("\nFinal Matrix: \n\n",matrix) # For Test
    return matrix[n][m]

print("\nMinimum Number of Operations: ",edit_distance("fast","cats"), "\n")