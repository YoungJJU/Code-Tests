import sys
t = int(sys.stdin.readline())
for w in range(t):
    n = int(sys.stdin.readline())
    a = list(range(2,n+1))
    for i in a:
        if i != 0:
            for j in range(2*i,n+1,i):
                a[j-2] = 0
    for k in range(int(n/2),1,-1):
        if k in a and (n - k) in a:
            print(k,(n-k))
            break
