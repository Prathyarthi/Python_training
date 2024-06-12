# N = int(input())
# arr = list(map(int,input().split()))

# def max_pair(N,arr):
#     for i in range(len(arr)):
#         first = arr[i]
#         for j in range(1,len(arr)):
#             second = arr[j]
#             if (first + second) == 18 and (first>second):
#                 return first,second
            
# print(max_pair(N,arr))





N = int(input())
arr = list(map(int,input().split()))
pro = 0
dlist = []
k = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] + arr[j] == 18:
            if arr[i] > arr[j]:
                k = arr[i] * arr[j]

            if k>pro:
                pro = k
                dlist.append(arr[i])
                dlist.append(arr[j])
            
print(dlist)