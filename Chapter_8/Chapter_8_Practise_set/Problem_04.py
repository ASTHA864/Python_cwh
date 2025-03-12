# Q4. Write a recursive function to calculate the sum of first n natural numbers.

def sum_natural(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum    


   

n=int(input("Enter number:"))
result=sum_natural(n)
print(f"{result}")