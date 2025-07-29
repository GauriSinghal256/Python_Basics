# classes -> Basically it is a blueprint to create objects 
class Student:
    language = "Py"
    roll = 11232628


Gauri = Student()
Gauri.name = "Sweety"
print(Gauri.name , Gauri.roll , Gauri.language)
# Here language and roll are class attributes as they directly belongs to the class and name is object/instance attribute as they belong to the object

# Here if we do that 
Gauri.language = "Java"
print(Gauri.language)


# Self parameter 

class Employee:
    language = "Python"
    salary = 12000000

    def __init__(self , name , salary , language):
        self.name = name 
        self.salary = salary 
        self.language = language
        print("I am creating an object")

Sapna = Employee("Sapna" , 1300000 , "Java")
print(Sapna.name , Sapna.salary , Sapna.language)