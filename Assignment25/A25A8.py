#==Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and Phone Class.
class calculator:
    def add(num1,num2):
        return num1+num2
    def sub(num1,num2):
        return num1-num2

class calculator2(calculator):      # Inheritance
    def mul(num1,num2):
        return num1*num2
    def divi(num1,num2):
        return num1/num2

class phone:
    def __init__(self):
        pass
    def get_calling():
        return'calling'
    def get_sms():
        return'sms'
class smartphone(calculator2,phone):
    def __init__(self):
        pass

print(smartphone.add(15,8))
print(smartphone.sub(8,3))
print(smartphone.mul(8,6))
print(smartphone.divi(49,7))
print(smartphone.get_calling())
print(smartphone.get_sms())