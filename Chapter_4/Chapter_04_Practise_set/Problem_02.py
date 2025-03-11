# Q2. Write a program to accept the marks of 6 students and display them in a sorted manner.

# marks=[23,45,43,67,89,22]
# marks.sort()
# print(marks)

students =[]

s1=int(input("Enter marks of student 1: "))
students.append(s1)

s2=int(input("Enter marks of student 2: "))
students.append(s2)

s3=int(input("Enter marks of student 3: "))
students.append(s3)

s4=int(input("Enter marks of student 4: "))
students.append(s4)

s5=int(input("Enter marks of student 5: "))
students.append(s5)

s6=int(input("Enter marks of student 6: "))
students.append(s6)

print(f"Students marks are: {students}")
students.sort()
print(f"Sorted students marks are: {students}")
