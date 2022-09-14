#==Write a python script to update 2nd Question, add a class variable (platform) and
#   create a classmethod to access it.


class profile:
    plateform="class variable"
    def __init__(self):
        self.name='ari'
        self.email="jhfh@.c"
        self.age=26
    @classmethod
    def get_plateform(cls):
        return cls.plateform

p1=profile()
print(p1.plateform)
print(profile.plateform)
print(p1.get_plateform())
print(profile.get_plateform())       # gives error ///use @classmethod 
