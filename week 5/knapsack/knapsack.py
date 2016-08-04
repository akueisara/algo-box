def optimal_weight(W, w):
    c = [0] * (W+1)
    for i in range(len(w)):
        for j in range(W, w[i]-1, -1):
            c[j] = max(c[j], c[j - w[i]] + w[i])
    return c[W]

if __name__ == '__main__':
    W, n = list(map(int, raw_input().split()))
    w = list(map(int, raw_input().split()))
    print(optimal_weight(W, w))
