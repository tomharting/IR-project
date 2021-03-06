import numpy as np
import sys

# Executes the shifted alignment algorithm on 2 queries

def create_normalized_matrix_M(query, target, iS, iE):
    m = len(query)
    n = len(target)
    scol = max(m, n)
    length_difference_query_target = abs(m-n)
    srow = length_difference_query_target + iS + iE + 1
    M = np.zeros(shape=(srow, scol))
    zero_query_row = np.concatenate((np.zeros(scol+iE), query, np.zeros(scol+iS)))
    for i in range(0,srow):
        leftIndex = scol+iE + iS - i
        rightIndex = leftIndex + scol
        zero_query_part = zero_query_row[leftIndex:rightIndex]
        non_zer_query_part_id = np.nonzero(zero_query_part)[0]
        first_el = non_zer_query_part_id[0]
        last_el = non_zer_query_part_id[len(non_zer_query_part_id)-1]+1
        M[i, first_el:last_el] = zero_query_part[first_el:last_el] / target[first_el:last_el]
    return M

def calculate_matrix_D(M, penalty_i, penalty_d):
    (srow, scol) = M.shape
    D = np.zeros(shape=(srow,scol))
    for j in range(1, scol):
        for i in range (0, srow):
            if M[i,j] != 0.:
                D[i, j] = calculate_postition_matrix_D(D, M, i, j, srow, penalty_i, penalty_d)
    return D


def calculate_postition_matrix_D(D, M, i, j, srow, penalty_i, penalty_d):
    del_val = deletion(D,M,i,j, penalty_d)
    ins_val = insertion(D,M,i,j, srow, penalty_i)
    prev_val = previous(D,M,i,j)
    min_val = min([del_val, ins_val,prev_val])
    if min_val == sys.maxint:
        return 0.0
    return min_val


def previous(D, M, i, j):
    d = D[ i, j - 1]
    m_i_j = M[ i, j]
    m_i_j1 = M[ i, j - 1]
    if m_i_j1 == 0 or m_i_j == 0:
        return sys.maxint
    else:
        return d + abs(m_i_j / m_i_j1 - 1)


def deletion(D, M, i, j, deletion_penalty):
    if i == 0 or j < 2:
        return sys.maxint
    else:
        d = D[ i - 1, j - 2]
        m_i1_j1 = M[ i - 1, j - 1]
        m_i_j = M[ i, j]
        m_i_j1 = M[ i, j - 1]
        m_i1_j2 = M[ i - 1, j - 2]
        if m_i1_j1 == 0.0 or m_i_j == 0.0 or m_i1_j2 == 0 or m_i_j1 == 0:
            return sys.maxint
        else:
            return d + abs((((m_i1_j1 * m_i_j)) / (m_i1_j1 + m_i_j)) * (
                    1 / ((m_i1_j2 * m_i_j1) / (m_i1_j2 + m_i_j1))) - 1) + deletion_penalty
        return del_val

def insertion(D, M, i, j, srow, insert_penalty):
    if j < 1 or i == (int(srow) - 1):
        return sys.maxint
    else:
        d = D[ i + 1, j - 1]
        m_1i_j = M[ i + 1, j]
        m_i_j = M[ i, j]
        m_1i_j1 = M[ i + 1, j - 1]
        m_i_j1 = M[ i, j - 1]
        if m_1i_j == 0.0 or m_i_j == 0.0 or m_1i_j1 == 0 or m_i_j1 == 0:
            return sys.maxint
        else:
            return d + abs((m_1i_j + m_i_j) / (m_1i_j1 + m_i_j1) - 1) + insert_penalty

# Retrieves the lowest value from matrix D leaving out zero values in M.
def getMinVal(D, M):
    (row_size, col_size) = D.shape
    min_val = sys.float_info.max
    for i in range(0,row_size):
        for j in range(col_size-1, 1, -1):
            if M[i,j] != 0. and M[i,j-1] != 0.:
                if D[i,j] < min_val:
                    min_val = D[i,j]
                break
    return min_val


# Compares a query with a target
def compare_IOI_vectors(query, target, penalty_i, penalty_d):
    if len(query) > len(target):
            tmp = query
            query = target
            target = tmp
    iS = 1
    iE = 2

    # if query is smaller then our paddings we should decrease the paddings
    if len(query) <= max(iS,iE):
        iS = len(query) -1
        iE = iS

    M = create_normalized_matrix_M(query, target, iS, iE)
    D = calculate_matrix_D(M, penalty_i, penalty_d)
    return getMinVal(D, M)

