class Person():
    name="Willian"

    #allows me to call this without ()
    @property
    def myName(self):
        return self.name

#positional argument passing to function
def printNum(a,b,c):
    print('A: ',a)
    print('B: ',b)
    print('C: ',c)

#keyword argument, doesn't matter the order
def printName(kwargName=None, kwargLast=None):
    print("Name: ",kwargName)
    print('Last Name: ',kwargLast)
def sendEmail(sender,receiver):
    print(sender)
    print(receiver)

printNum(1,2,3)
name = 'Willian'
lastName = "Angola"
printName(name,lastName)
#more explanatory than just pass parameters
sendEmail(sender='wsadevv@f3.com',receiver='no@ga.com')

p = Person()
print(p.myName)
