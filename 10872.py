t = int(input())
def factorial(t):
    if t == 0:
        return 1
    else:
        return factorial(t-1)*t
print(factorial(t))
