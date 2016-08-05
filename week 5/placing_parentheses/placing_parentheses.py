# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinMax(i, j, op, m, M):
    mmin = float("inf")
    mmax = float("-inf")
    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], op[k])
        b = evalt(M[i][k], m[k+1][j], op[k])
        c = evalt(m[i][k], M[k+1][j], op[k])
        d = evalt(m[i][k], m[k+1][j], op[k])
        mmin = min(mmin, a, b, c, d)
        mmax = max(mmax, a, b, c, d)
    return(mmin, mmax)		
		
def get_maximum_value(dataset):
    op = dataset[1:len(dataset):2]
    digit = dataset[0:len(dataset)+1:2]
    n = len(digit)
    m = [[0 for i in range(n)] for j in range(n)]
    M = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        m[i][i] = int(digit[i])
        M[i][i] = int(digit[i])
    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = MinMax(i,j,op,m,M)
    return M[0][n-1]

if __name__ == "__main__":
    print(get_maximum_value(raw_input()))
