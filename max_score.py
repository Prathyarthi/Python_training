n = int(input("Enter n: "))

arr = list(map(int,input("Element: ").split()))
arr.sort()

res = []

start = 0
end = -1

while len(arr)>=1:
    res.append(abs(arr[end]-arr[start]))
    arr.pop(start)
    arr.pop(end)

print(sum(res))