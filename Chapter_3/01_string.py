#Slicing

name1='Anshika'
print(name1[1:5])
print(name1[0:])
print(name1[:7])
print(name1[-4:-1])

#slicing with skip values
print(name1[0:6:2])


#String Function

#1. len()
#2. capitalize() , startswith("as") ,endswith("a")
name2="astha"
print(len(name2))
print(name2.capitalize())
print(name2.startswith("as"))
print(name2.endswith("a"))

#3. lower() , upper() 
print(name2.lower())
print(name2.upper())

#4. title() - Capitalize first character
title_name="smart  cart"
print(title_name.title())

#5. string.find(word)
#6. string.replace(oldword, newword)
print(title_name.find("cart")) #return index of first occurence of word
print(title_name.replace("cart","deal"))


#7. strip() - remove leading and trailing whitespace
#8. lstrip() - remove leading  whitespace
#9. rstrip() - remove trailing whitespace
name3='''  Khushi   '''
print(name3.strip())
print(name3.lstrip())
print(name3.rstrip())

#10. zfill(5)- Pads the string with zeroe on the left
print(name3.zfill(15))

