def get_change(n):
    #write your code here
    result = 0
    result += int(n/10)
    n = n % 10
    result += int(n/5)
    n = n % 5
    n = n + result
    return n

if __name__ == '__main__':
    n = int(input())
    print(get_change(n))