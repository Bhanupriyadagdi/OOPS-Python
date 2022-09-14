#==Write a python script to create a Calculator class with 2 methods for adding and
#  subtracting 2 values.
class calculator:
    def add(num1,num2):
        return num1+num2
    @staticmethod
    def sub(num1,num2):
        return num1-num2



print(calculator.add(8,5))
print(calculator.sub(4,5))
