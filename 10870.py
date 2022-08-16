t = int(input())
def pibo(t):
    if t == 0:
        return 0
    if t == 1 or t == 2:
        return 1
    else:
        return pibo(t-1) + pibo(t-2)
print(pibo(t))
