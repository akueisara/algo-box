def optimal_summands(n):
    summands = []
    if(n<=2):
        summands.append(n)
    else:
        l = 1
        while(n > 2*l):
            summands.append(l)
            n -= l
            l += 1
        summands.append(n)
    #write your code here
    return summands

if __name__ == '__main__':
    n = int(raw_input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print str(x) + " ",
