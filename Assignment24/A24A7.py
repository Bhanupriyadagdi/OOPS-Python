#==Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,hdd) and 
# 2 methods (showConfig() to print the values, __init__() to initialize the values).
class Laptop:
    def __init__(self):
        self.brand="Lenova"
        self.ram= '8GB'
        self.cpu= 'i7'
        self.hdd= '1TB'
    def show(self):
        print(self.brand,self.ram)
    def config(self):
        print(self.cpu,self.hdd)

l1=Laptop()
l1.show()
Laptop.config(l1)