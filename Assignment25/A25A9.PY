#===Write a python script to create an application like Truecaller where names and
#   numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a
#   number and 2nd to add a new entry).
class Truecaller:
    numberdiary={123:'ali',234:'bie',345:'cari',845:'geo',995:'den'}
    
    @classmethod
    def fetch_number(cls,number):
        if number in cls.numberdiary:
            print(cls.numberdiary[number])
        else:
            print("unknown")
            
    @classmethod
    def add_newentry(cls,name,number):
        if number not in cls.numberdiary:
            cls.numberdiary[number]=name
        

Truecaller.add_newentry('ali',741)
Truecaller.fetch_number(123)
print(Truecaller.numberdiary)

