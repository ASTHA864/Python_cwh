# Q10. Write a program to print  multiplication table of a given number using for loop in reverse order.

num=int(input("Enter number:"))

for i in range(10,0,-1):
    result=num*i
    print(f"{num} * {i} = {result}")
