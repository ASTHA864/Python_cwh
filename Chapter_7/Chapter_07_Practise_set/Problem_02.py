# Q2. Write a program to great all person names stored in a list 'l' and which starts with S.

l=["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if(name.startswith("S")):
        print(f"Good Morning {name}")
