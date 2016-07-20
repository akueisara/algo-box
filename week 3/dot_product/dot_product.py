def min_dot_product(a, b):
    #write your code here
    res = 0
    a.sort()
    b.sort()
    for i in range(len(a)):
        res += a[i] * b[len(a)-i-1]
    return res

if __name__ == '__main__':
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    b = list(map(int, raw_input().split()))
    print(min_dot_product(a, b))