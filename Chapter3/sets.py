s = {1,5,23,5,6,7,7,7 , "Gauri"}

# create an empty set 
e = set()
print(s)

s.add(345)
print(s)
print(len(s))
s.remove("Gauri")
print(s)
# s.clear()
# s.pop() -> Remove a random element from the set 

# Union in sets 
s1 = {1,2,3,7}
s2 = {4,5,6,1,7}
s3 = {3,7}
print(s1.union(s2))

# intersection 
print(s1.intersection(s2))
print(s1-s2)
print(s2-s1)
print(s3.issubset(s1))
print(s1.issuperset(s3))

