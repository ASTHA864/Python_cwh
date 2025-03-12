
'''
factorial (n) = n * factorial(n-1) 
factorial 0 = 1
factorial 1 = 1
factorial 2 = 2 X 1
factorial 3 = 3 X 2 X 1

'''


def fact(n):
    if(n==0 or n==1):
        return 1
    return n * fact(n-1)

n= int(input("Enter a number:"))
print(f"The factorial of this number is: {fact(n)}")