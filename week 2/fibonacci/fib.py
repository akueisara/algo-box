# Uses python3
def calc_fib(n):
    if n <= 1:
        return n
    elif n == 2:
        return 1
    else:
        result = [0] * (n+1)
        result[1] = 1
        result[2] = 1
        for i in xrange(3,n+1):
            result[i] = result[i-1] + result[i-2]
        return result[n]

n = int(input())
print(calc_fib(n))