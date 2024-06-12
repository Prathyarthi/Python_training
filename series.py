def f(N):
    if N==0 or N==1:
        return 1
    return (f(N-1)*f(N-1) + (N-2)*(N-2)) % 47

N = int(input())
print(f(N))

