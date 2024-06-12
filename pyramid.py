N = int(input())
res = N*1
num = 2
for i in range(N-1,0,-1):
    res+=2*num*i
    num+=1

print(res)