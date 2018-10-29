def min_matrix_paranthesization(p): # p is a list of matrix sizes where matrix i has dimensions P[i-1]xP[i]
    n = len(p) - 1
    m = [[-1 for i in range(n+1)] for i in range(n+1)]
    s = [[-1 for i in range(n + 1)] for i in range(n + 1)]
    for i in range(1,n+1):
        for j in  range(1,n+1):
            if i == j:
                m[i][j] = 0
    for l in range(2,n+1):
        for i in range(1,(n-l+1)+1):
            j = i+l-1
            for k in range(i,j):
                q = m[i][k] + m[k+1][j] + p[i-1]* p[k] * p[j]
                if m[i][j] == -1:
                    m[i][j] = q
                    s[i][j] = k
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m,s

def print_optimal_paranthesization(s,i,j):
    if i == j:
        print ("A"+str(i),end='',flush=True)
    else:
        print("(",end='',flush=True)
        print_optimal_paranthesization(s,i,s[i][j])
        print_optimal_paranthesization(s,s[i][j]+1,j)
        print(")",end='',flush=True)
