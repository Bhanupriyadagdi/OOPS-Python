#==Write a python program to create 3 user objects and find the youngest of all.
def compare(x,y,z):
    if x>y and x>z:
        print("The youngest is Aki")
    elif y>x and y>z:
        print("The youngest is Tom")
    else:
        print("The youngest is Ari")

class student:
    def __init__(self,age):
        self.age=age
        

Aki =student(18)
Tom=student(17)
Ari=student(19)
compare(Aki.age,Tom.age,Ari.age)

