# Q.7 Write a program to find out whether a given post is talking about "Astha"or not.

post=input("Enter the post:")

if("Astha".lower() in post.lower()):
    print("Given post is talking about Astha")
else:
    print("Given post is not talking about Astha")    