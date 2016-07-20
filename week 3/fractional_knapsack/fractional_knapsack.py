def get_best_idx(ratios):
    best = 0.0
    best_idx = 0
    for i in xrange(len(ratios)):
        if ratios[i] > best:
            best = ratios[i]
            best_idx = i
    return best_idx

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    ratios = [0.]*len(weights)
    for i in xrange(len(weights)):
        ratios[i] = float(values[i])/weights[i]
    while (capacity > 0):
        best_idx = get_best_idx(ratios)
        if (weights[best_idx] > 0):
            a = min(float(capacity), float(weights[best_idx]))
            ratio = float(values[best_idx])/ weights[best_idx]
            value += a * ratio
            weights[best_idx] -= a
            capacity -= a
            if (weights[best_idx] == 0):
                del weights[best_idx]
                del values[best_idx]
                del ratios[best_idx]
    return value


if __name__ == "__main__":
    data = list(map(int, raw_input().split()))
    n, capacity = data[0:2]
    values = [0]*n
    weights = [0]*n
    for i in range(n):
        values[i], weights[i] = map(int, raw_input().split())
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))