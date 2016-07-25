def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    a.sort()
    count, element = 1, -1
    for i in range(len(a)):
        if(a[i] == element):
            count += 1
        else:
            element = a[i]
            count = 1
        if(count > len(a)/2):
            return 1
    return -1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, raw_input().split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
