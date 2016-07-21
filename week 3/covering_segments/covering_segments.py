from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments = sorted(segments, key=lambda segment: segment.end)
    current = segments[0].end
    points.append(current)
    for s in segments:
        if ((current < s.start) or (current > s.end)):
            current = s.end
            points.append(current)
    return points

if __name__ == '__main__':
    n = int(raw_input())
    data = [0] * (2*n)
    for i in range(n):
        data[2*i], data[2*i+1] = map(int, raw_input().split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print str(p) + " ",