#==Write a python program to create a School class and 3 instance variables and 1 class variable.
class school:
     #class variable sn
    sn="Geetanjali school kharwa"  

    # instance variable name,age and id         
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id

st1=school('mohit',14,202)

print(school.sn)
print("student name:",st1.name)
print("student age:",st1.age)
print("student id:",st1.id)
