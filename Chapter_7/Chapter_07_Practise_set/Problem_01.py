
# Q1. Write a program to print multiplication table of a given number using for loop.
 
num=int(input("Enter number:"))

for i in range(1,11):
    result=num*i
    print(f"{num} * {i} = {result}")
    i+=1