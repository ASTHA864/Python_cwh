

s={5,3,6,5,6,3,2}
s.add(4)
s.add(8)
print(s)
print(s.clear()) #removes all elements from the set
print(s) #returns an empty set

s1={5,3,6,2,32,1, "khushi"}

s2={5,3,6,9,11}
print(s1.difference(s2)) #returns a set containing the difference between two or more sets
print(len(s1))
print(s1.remove(5)) #removes the specified element from the set
print(s1)

print(s1.pop()) #removes an element from the set
print(s1)
