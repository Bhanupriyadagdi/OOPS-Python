#==Write a python program to delete the age property of the user.
class student:
    def __init__(self):
        self.name='Devil'
        self.age=15


st1=student()
del(st1.age)
print(st1.name)
print(st1.age)

