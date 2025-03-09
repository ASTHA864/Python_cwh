#List - Mutuable

l1=[1,3,5,2,6,9,"python",3.14]
print(l1)
# l1.sort() #sort the list

l1.reverse() #reverse the list
print(l1)
l1.append(12) #add element at the end of the list
print(l1.insert(2,5)) #insert element at the given index
print(l1)
print(l1.pop(1)) #remove element at the given index
print(l1)
print(l1.remove(3.14)) #remove element from the list

print(l1[1:3]) #slicing
print(l1[0]) #slicing with step

