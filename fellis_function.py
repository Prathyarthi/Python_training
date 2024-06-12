def f(N):
    if N==0 or N==1:
        return 1
    return (f(N-1) + 7*f(N-2) + (N//4) % (10**9 + 7))

N = int(input())
print(f(N))

