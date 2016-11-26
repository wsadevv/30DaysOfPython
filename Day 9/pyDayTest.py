import datetime


class MessageUser():
    userDetails = []
    messages = []
    baseMessage = """Hi {name}!
    Thank you for the purchase on {date}.
    We hope you are exicted about using it. Just as a
    reminder the purcase total was ${total}.
    Have a great one!
    Team wsadevv
    """
    def addUser(self, name, amount,email=None):
        #[1:] from 1 to last
        name[0].upper()+name[1:].lower()
        amount = "%.2f" %(amount)
        detail ={
            "name": name,
            "amount": amount,
        }
        today = datetime.date.today()
        dateText = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = dateText
        if email is not None:
            detail['email'] = email
        self.userDetails.append(detail)
    def getDetails(self):
        return self.userDetails

    def makeMessages(self):
        if len(self.userDetails) > 0:
            for detail in self.getDetails():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.baseMessage
                newMessage = message.format(
                    name=name,
                    date = date,
                    total=amount

                )
                self.messages.append(newMessage)
            return self.messages
        return []
def crazyS():
    print("Successfuly imported brah!")

users = MessageUser()
users.addUser("Justin",123.32)
users.addUser("John",94.23)
users.addUser("Sean",93.23)
users.addUser("Emilee",193.32)
users.addUser("Justin",13.23)
users.addUser('Will', 155.32,email="wsadevv@jinchuriki.com")


default_names = ['Justin', 'John', 'Emilee',
                 'Jim', 'ron', 'Sandra', 'VeRonica', 'withney']
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]
