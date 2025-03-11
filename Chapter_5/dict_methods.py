#Dictonary method

# dict={}- empty dictionary
# dict={key:value} - dictionary with one key value pair

marks= {
  "student1": 23,
  "student2": 45,
  "student3": 43,
}
print(len(marks)) #returns the number of items in the dictionary
print(marks.items()) #returns a list containing a tuple for each key value pair
print(marks.keys()) #returns a list containing the dictionary's keys
print(marks.values()) #returns a list containing the values of the dictionary
marks.update({"student1": 50 ,"student4": 60}) #update the dictionary with the specified key-value pairs
print(marks)

print(marks.get("student2")) #returns the value of the specified key #returns None if the key does not exist
print(marks["student2"]) #returns the value of the specified key  #throws an error if the key does not exist