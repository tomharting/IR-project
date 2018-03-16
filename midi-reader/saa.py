#shifted alignment algorithm
import numpy as np
from numpy import array

def normvector(ioivector):
    #For instance,  may be set to a value from m-2 to m+2 in order to deal with possible insertions and deletions in the
    # query input. Thus all these variant normalized versions of the IOI vectors for a song must be compared for similarity
    # with the query IOI vector.
    return ioivector

def normM(query, target):
    m = len(query)
    n = len(target)
    scol = min(m, n)
    isieMin = abs(m-n)
    iS = 1
    iE = 2
    srow = isieMin + iS + iE + 1
    M = np.zeros(shape=(srow, scol))
    for i in range(0,srow):
        for j in range (0,scol):
            qindex = iS - i + j
            # print(iS, qindex, i, j)
            if 0 <= qindex <= min(m, n) - 1:
                M[i, j] = query[qindex] / target[j]
            else:
                M[i, j] = 0
    return M

def calcD(M):
    (srow, scol) = M.shape
    D = np.zeros(shape=(srow,scol))
    D[:, 0] = 0.0
    # print D
    for j in range(1, scol):
        for i in range (0, srow):
            print (i,j)
            print (' before', D)
            D[i, j] = dynamicD(D, M, i, j)
    return D

def dynamicD(D, M, i, j):
    penalty1 = 0.25
    penalty2 = 0.25
    vals = []
    d1b = True
    d3b = True
    (srow, scol) = np.shape(M)
    if i == 0 or j < 2:
        # dont use deletion
        d1b = Falsez
        print('d1b = false')
    if j < 1 or i == (int(srow)-1):
        # dont use insertion
        d3b = False
        print('d3b = false')
    if d1b:
        d3 = getVal(D, i - 1, j - 2) + abs((
                    (getVal(M, i - 1, j - 1) * getVal(M, i, j)) /
                    (getVal(M, i - 1, j - 1) + getVal(M, i, j))
                ) * (1 / (
                    (getVal(M, i - 1, j - 2) * getVal(M, i, j - 1)) /
                    (getVal(M, i - 1, j - 2) + getVal(M, i, j - 1))
                )) - 1) + penalty2
        vals.append(d3)
    if d3b:
        d2 = getVal(D, i + 1, j - 1) + abs(
            ((getVal(M, i + 1, j) + getVal(M, i, j)) / (getVal(M, i + 1, j - 1) + getVal(M, i, j - 1))) - 1) + penalty1
        vals.append(d2)

    d1 = getVal(D, i, j - 1) + abs((getVal(M, i, j) / getVal(M, i, j - 1)) - 1)
    vals.append(d1)

    return min(vals)


def getVal(matrix, i, j):
    # print (i,j,np.shape(matrix))
    (xi, xj) = matrix.shape
    # print(i, int(xi), j, int(xj))
    if i < int(xi) and j < int(xj):
            return matrix[i,j]
    else:
        print('error: not the right indexes')
        return 0.1

query = np.array([1.0, 2.0, 3.0, 2.0, 2.0, 2.0])
target = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])

queryn = normvector(query)
targetn = normvector(target)

M = normM(queryn, targetn)
print M

D = calcD(M)
print D


