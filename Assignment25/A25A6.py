#===WAPS to create a Calculator 2.0 class with 2 methods for multiplication
#   and division of 2 values and inherit it from the Calculator class.
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

print(calculator2.mul(4,5))
print(calculator2.divi(7,2))
print(calculator2.add(8,9))
print(calculator2.sub(9,6))