print("welcome to blackpink bank")

class Atm(object):
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, withdraw):
        print("money withdrawn")

    def increase(self, increase):
        print("money added")

    def showbalance(self):
        print("balance")

    cardNumber = input("enter card number")
    cardPass = input("enter password")

