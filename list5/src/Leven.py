import numpy as np

DEFAULT_OPERATION_COST = 1

def GetMinimumOperations(matrix, i, j):
    insert = matrix[i][j - 1] + 1
    delete = matrix[i - 1][j] + 1
    replace = matrix[i - 1][j - 1] + 1
    
    return min(insert, delete, replace)

def LevSim(word1, word2):
    matrix = np.zeros((len(word1), len(word2)))
    
    for i in range(1, len(word1)):
        for j in range(1, len(word2)):
            if word1[i - 1] == word2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = GetMinimumOperations(matrix, i, j)
    
    return matrix[len(word1) - 1][len(word2) - 1]
