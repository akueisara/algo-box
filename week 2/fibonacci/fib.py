# Uses python3
def calc_fib(n):
    result = [0] * (n+1)
    result[0] = 0
    result[1] = 1
    for i in xrange(2,n+1):
        result[i] = result[i-1] + result[i-2]
    return result[n]

n = int(input())
print(calc_fib(n))