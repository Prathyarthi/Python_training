def diwali(n,p):
    contest = 4*60

    travel_time = p

    remaining_time = contest - travel_time

    time_per_problem = [5*i for i in range(1,n+1)]

    count = 0

    for i in time_per_problem:
        if remaining_time>=i:
            remaining_time-=i
            count+=1
        else:
            break

    return count

n = int(input())
p = int(input())
print(diwali(n,p))