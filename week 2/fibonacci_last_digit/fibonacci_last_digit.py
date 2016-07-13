# Uses python3

def get_fibonacci_last_digit(n):
    result = [0]*(n+1)
    result[0] = 0
    result[1] = 1
    for i in xrange(2,n+1):
        result[i] = (result[i-1] + result[i-2]) % 10
    return result[n]

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit(n))
