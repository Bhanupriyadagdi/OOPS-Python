#==Write a python script to update 2nd Question, change email and age to __email and __age.
class profile:
    def __init__(self):
        self.name="bhanu"
        self.__email="bhpd22@g.com"        #_ _ is used for hide  the data,can't access outside
        self.__age=26

    def get_email(self):
        return self.__email
    def get_age(self):
        return self.__age


p1=profile()

print(p1.name)
print(p1.get_email())
print(p1.get_age())
print(p1.__email)
print(p1.__age)
