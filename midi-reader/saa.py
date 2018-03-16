#shifted alignment algorithm
import numpy as np
import sys
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
    for j in range(1, scol):
        for i in range (0, srow):
            print (i,j)
            D[i, j] = dynamicD(D, M, i, j)
    return D


def dynamicD(D, M, i, j):
    del_val = deletion(D,M,i,j)
    ins_val = insert(D,M,i,j)
    prev_val = previous(D,M,i,j)
    min_val = min([del_val, ins_val,prev_val])
    if min_val == sys.maxint:
        return 0.0
    return min_val


def previous(D, M, i, j):
    d = getVal(D, i, j - 1)
    m_i_j = getVal(M, i, j)
    m_i_j1 = getVal(M, i, j - 1)
    if m_i_j1 == 0 or m_i_j == 0:
        return sys.maxint
    else:
        return d + abs(m_i_j / m_i_j1 - 1)


def deletion(D, M, i, j):
    deletion_penalty = 0.25
    if i == 0 or j < 2:
        return sys.maxint
    else:
        d = getVal(D, i - 1, j - 2)
        m_i1_j1 = getVal(M, i - 1, j - 1)
        m_i_j = getVal(M, i, j)
        m_i_j1 = getVal(M, i, j - 1)
        m_i1_j2 = getVal(M, i - 1, j - 2)
        if m_i1_j1 == 0.0 or m_i_j == 0.0 or m_i1_j2 == 0 or m_i_j1 == 0:
            return sys.maxint
        else:
            return d + abs((((m_i1_j1 * m_i_j)) / (m_i1_j1 + m_i_j)) * (
                    1 / ((m_i1_j2 * m_i_j1) / (m_i1_j2 + m_i_j1))) - 1) + deletion_penalty
        return del_val

def insert(D, M, i, j):
    (srow, scol) = np.shape(M)
    insert_penalty = 0.25
    if j < 1 or i == (int(srow) - 1):
        return sys.maxint
    else:
        d = getVal(D, i + 1, j - 1)
        m_1i_j = getVal(M, i + 1, j)
        m_i_j = getVal(M, i, j)
        m_1i_j1 = getVal(M, i + 1, j - 1)
        m_i_j1 = getVal(M, i, j - 1)
        if m_1i_j == 0.0 or m_i_j == 0.0 or m_1i_j1 == 0 or m_i_j1 == 0:
            return sys.maxint
        else:
            return d + abs((m_1i_j + m_i_j) / (m_1i_j1 + m_i_j1) - 1) + insert_penalty


def getVal(matrix, i, j):
    # print (i,j,np.shape(matrix))
    (xi, xj) = matrix.shape
    # print(i, int(xi), j, int(xj))
    if i < int(xi) and j < int(xj):
            return matrix[i,j]
    else:
        print('error: not the right indexes')
        return 0.0

query = np.array([1.0, 2.0, 3.0, 2.0, 2.0, 2.0])
target = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])

queryn = normvector(query)
targetn = normvector(target)

M = normM(queryn, targetn)
print M

D = calcD(M)
print D


