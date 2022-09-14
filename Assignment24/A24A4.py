#==Write a python program to init default values for user object using __init__ method.
class school:
    def __init__(self):
        self.schoolname="Geetanjali school"
        self.scholernumber=227856
        
student1=school()
student2=school()
print(student1.schoolname,student1.scholernumber,sep='\n')

print(student2.schoolname,student2.scholernumber,sep='\n')
