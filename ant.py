# arr = [-1,1,-1,1,-1,1]
arr = [1,-1,1,-1,1,-1]
count = 0
n = len(arr)

a = arr[0]
for i in range(n):
    if arr[i]==a:
        count+=1
print(count)
