def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a+b+c)/3
    print(average)

# avg() 

def goodDay(name):
    print(f"Good Day {name}")

goodDay("Gauri")    

def add(a , b=5):
    print(a+b)

add(2)    

# Recursion 
def fact(n):
    if(n<=1):
        return 1
    return n*fact(n-1)


print(fact(5))