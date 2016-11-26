#import from my files -> class i.e
#from pyDayTest import MessageUser
from pyDayTest import crazyS
#or
#importing from a module
from pyDayMod.makeMessages import MessageUser

users = MessageUser()
users.addUser("Justin",123.32)
users.addUser("John",94.23)
users.addUser("Sean",93.23)
users.addUser("Emilee",193.32)
users.addUser("Justin",13.23)
users.addUser('Will', 155.32,email="wsadevv@jinchuriki.com")
print(users.getDetails())
print(users.makeMessages())
crazyS()
