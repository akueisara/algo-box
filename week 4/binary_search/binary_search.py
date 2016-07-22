def binary_search(a, x):
    low, high = 0, len(a) - 1
    a.sort()
    while(low <= high):
        mid = low + (high - low)/2
        if (x == a[mid]):
            return mid
        elif (x < a[mid]):
            high = mid - 1
        else:
            low = mid + 1
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    data = list(map(int, raw_input().split()))
    n = data[0]
    a = data[1 : n + 1]
    datax = list(map(int, raw_input().split()))
    m = datax[0]
    x = datax[1 : m + 1]	
    for i in range(len(x)):
        # replace with the call to binary_search when implemented
        # print str(linear_search(a, x[i])) + ' ',
        print str(binary_search(a, x[i])) + ' ',
