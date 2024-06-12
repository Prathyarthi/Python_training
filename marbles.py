N,A,B = list(map(int,input("Marbles: ").split()))

count = set()
for i in range(N//A+1):
    for j in range(N//B+1):
        mcount = N-A*i-B*j
        if mcount>0:
            count.add(mcount)

print(len(count))
print(count)