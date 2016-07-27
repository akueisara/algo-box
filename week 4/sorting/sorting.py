import random

def partition3(a, l, r):
    x = a[l]
    m1 = l
    m2 = r
    i = l
    while(i <= m2):
        if (a[i] < x):
            a[i], a[m1] = a[m1], a[i]
            m1 += 1
            i += 1
        elif (a[i] > x):
			a[i], a[m2] = a[m2], a[i]
			m2 -= 1
        else:
			i += 1
	m = [m1, m2]
    return m

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    # m = partition2(a, l, r)
    # randomized_quick_sort(a, l, m - 1)
    # randomized_quick_sort(a, m + 1, r)
    m = partition3(a, l, r)
    randomized_quick_sort(a, l, m[0] - 1)
    randomized_quick_sort(a, m[1] + 1, r)


if __name__ == '__main__':
    n = int(input())
    a = [0] * n
    a = list(map(int, raw_input().split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print str(x) + ' ',