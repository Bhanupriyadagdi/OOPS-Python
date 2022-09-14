#==Define a class Employee with instance object variables empid, name, salary.
class employee:
    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary

    def show(self):
        print('employeeid:',e1.empid,'name:',e1.name,'salary:',e1.salary)

e1=employee(1234,'Denny',45000)
e1.show()