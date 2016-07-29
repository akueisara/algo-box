# originally from http://www.cnblogs.com/dm1299/p/5571108.html

from itertools import chain

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    a = zip(starts, [float('-inf')]*len(starts))
    b = zip(ends, [float('inf')]*len(ends))
    c = zip(points, range(len(points)))
    sortedlist = sorted(chain(a,b,c), key=lambda a : (a[0], a[1]))
    stack = []
    for i, j in sortedlist:
        if j == float('-inf'):
            stack.append(j)
        elif j == float('inf'):
            stack.pop()
        else: 
            cnt[j] = len(stack) 
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    data = list(map(int, raw_input().split()))
    n = data[0]
    m = data[1]
    starts = [0] * n
    ends = [0] * n
    for i in range(n):
        starts[i], ends[i] = map(int, raw_input().split())
    points = list(map(int, raw_input().split()))
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print str(x)+ ' ',
