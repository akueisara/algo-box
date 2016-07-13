# Uses python3

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b,a%b)

def lcm(a, b):
    #write your code here
    return a*b / gcd(a,b)

if __name__ == '__main__':
    a, b = map(int, raw_input().split())
    print(lcm(a, b))

