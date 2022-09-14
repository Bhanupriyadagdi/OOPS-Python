#==Write a python script to update the above Profile class with encapsulation.

class Profile:
    def __init__(self):
        self.name='Bhanu'
        self.email='bhpd736@g.com'
        self.age=26

    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
        return self.name

p1=Profile()
print(p1.get_name())
print(p1.set_name('Bhanupriya'))
print(p1.name)
        