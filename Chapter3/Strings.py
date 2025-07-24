a = 'Gauri Singhal'
b = "Gauri"
c = '''Gauri'''

# String is immutable in python 

# Slicing 
name = a[0:5]
print(name)

# skip value as a part of slice  
word = a[0:13:2]
print(word)

# Some functions of Strings
print(len(a))
print(a.endswith("ghal"))
print(a.startswith("Gauri"))
print(a.capitalize())
