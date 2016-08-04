def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def dp_sequence(n):
    sequence = []
    a = [0]*(n+1)
    for i in range(1,len(a)):
        a[i] = a[i-1] + 1
        if (i%2 == 0):
            a[i] = min(1+a[i/2], a[i])
        if (i%3 == 0):
            a[i] = min(1+a[i/3], a[i])
    while (n>1):
        sequence.append(n)
        if (a[n-1] == a[n]-1):
            n = n-1
        elif (n%2 == 0 and (a[n/2] == a[n]-1)):
            n = n/2		
        elif (n%3 == 0 and (a[n/3] == a[n]-1)):
            n = n/3
    sequence.append(1)
    return reversed(sequence)

n = int(input())
sequence = list(dp_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print str(x) + ' ',