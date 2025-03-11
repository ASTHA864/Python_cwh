# Q9. Can you change the values inside a list which is contained in a set S?
#No you cannot change the values inside a list.
# In fact, you cannot even have  list as an element in a set. (Immutable, and not hashable)
#  if we could then we can't change value by indexing.

s={8,7,12 , "python", [1,2]}

print(s[0])