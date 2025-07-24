l = ["Harry" , "Pottor" , "Superman" , "Spiderman"]

for name in l:
    if(name.startswith("S")):
        print(f"hello {name}")


n = int(input("Enter a number"))
i =1
while(i<11):
    print(f"{n} x {i} = {n*i}")   
    i+=1     


# Check whether a number is prime or not 
num = int(input("Enter the number"))
for i in range(2,num):
    if(num%i) == 0:
        print("Number is not prime") 
        break
else:
    print("Number is prime")
