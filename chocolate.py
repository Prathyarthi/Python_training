chocolates = list(map(int,input("Enter number of chocolates in each jar: ").split()))
N = len(chocolates)
count = 0

for i in chocolates:
    if i==0:
        continue
    if i%3==0:
        count = count + (i//3)
    else:
        count = count + (i//3) + 1

print(count)

