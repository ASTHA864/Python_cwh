# Q3. Write a program to print multiplication table of a given number using while loop.


num=int(input("Enter number:"))
i=1
while(i<11):
    result=num*i
    print(f"{num} * {i} ={result}")
    i+=1