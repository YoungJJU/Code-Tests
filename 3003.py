a = list(map(int,input().split()))
b = [1,1,2,2,2,8]
for i in range(6):
    b[i] = str(b[i] - a[i])
c = ' '.join(b)
print(c)
