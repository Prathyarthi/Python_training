n = int(input("Enter total number of students"))
grades = input("Grades: ")

p = int(input("Andrew's grade: "))
grade = str(grades[n-1])

if (n-p)>1:
    start = n-p-1
else:
    start = 0

if (n+p<=len(grades)):
    end = n + p
else:
    end = len(grades)

print(min(grades[start:end],key=lambda x : ord(x)),p)