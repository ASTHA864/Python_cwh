# Q5. Write a program to find the sum of first n natural numbers using while loop.

n=int(input("Enter number:"))
i=0
sum=0
while(i<=n):
    sum=sum+i
    i+=1
print(f"{sum}")    