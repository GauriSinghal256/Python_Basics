marks = {
    "Gauri": 100,
    "Shubham":90,
    "Rohan":34
}

print(marks,type(marks))
print(marks["Gauri"])
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Rohan": 78 , "Renuka":89})
print(marks)
print(marks.get("Gauri2")) #-> it will give us none
#print(marks["Gauri2"]) -> it will give us error

# marks.clear()
new_marks = marks.copy()

value = marks.pop("Rohan")
print(value)
print(marks)

item = marks.popitem();
print(item)
print(marks)

# Empty Dictionary 
d = {}