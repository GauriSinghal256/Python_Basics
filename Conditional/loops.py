for i in range(1,6):
    print(i) 

# while loop 
j=0
while(j<6):
    print(j)
    j+=1

k=0
l =[1,"gauri","sapna" ,23,45,67]
while(k<len(l)):
    print(l[k])
    k+=1


for i in range(0,len(l)):
    print(l[i])


for j in l:
    print(j)

tuple =(1,2,3,'j')
for h in tuple:
    print(h)

string = "Gauri"
for s in string:
    print(s)

# for loop with else 
for char in "ApnaCollege":
    print(char)
else:
    print("Done")    

# Break keyword 

for i in range(100):
    if(i==6):
        break 
    print(i)

 # Continue
for i in range(10):
    if(i==5):
        continue
    print(i) 