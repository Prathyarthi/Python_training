def most_freq(arr,n):
    max_freq = 0
    most_frequent = -1

    for i in range(n):
        count_freq = 1
        for j in range(n):
            if arr[j]==arr[i]:
                count_freq+=1

        if max_freq<count_freq:
            max_freq = count_freq
            most_frequent = arr[i]
        elif max_freq == count_freq:
            most_frequent = min(most_frequent,arr[i])
    return most_frequent

n = int(input("Enter number of voters: "))
arr = list(map(int,input("Enter votes: ").split()))

print("Winner: ", most_freq(arr,n))