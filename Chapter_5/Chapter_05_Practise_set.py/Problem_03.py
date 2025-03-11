# Q3. Can we have a set with 18(int) and "18"(str) as a value in it?
# Yes, we can have a set with 18(int) and "18"(str) as a value in it.

s=set()
s.add(18)

s.add("18")
print(s,type(s))

s1={18}
print(s1,type(s1))
s2={"18"}
print(s2,type(s2))
print(s1==s2)

