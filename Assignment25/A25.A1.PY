#==Write a python script to create a Profile class with 3 attributes (name, email, age):
class Profile:
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age


p1=Profile('Denny','a22@g.com',26)
print(p1.name)
print(p1.email)
print(p1.age)