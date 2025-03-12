# Q1. Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if(a>b and a>c):
        return f"a is greater {a}"
    elif(b>a and b>c):
        return f"b is greater {b}"
    else:
        return f"c is greater {c}"


a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
great= greatest(a,b,c)
print(great)