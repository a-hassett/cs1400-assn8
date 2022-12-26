# Alexandra Hassett, CS 1400

class PiggyBank:
    # initialize the money balance in the piggy bank and whether or not it is broken
    def __init__(self):
        self.__balance = 0
        self.__broken = False

    # make a new attribute that's equal to balance but can be used outside the class
    def setBalance(self, balance):
        self.__balance = balance
    def getBalance(self):
        return self.__balance
    balance = property(getBalance, setBalance)

    # make a new attribute that's equal to whether it's broken or not but can be used outside the class
    def setBroken(self, broken):
        self.__broken = broken
    def getBroken(self):
        return self.__broken
    broken = property(getBroken, setBroken)

    # when money is deposited into the piggy bank, add it to the amount before unless the piggy bank is broken
    def deposit(self, dispensedAmount):
        self.__balance += dispensedAmount
        if self.__broken:
            self.__balance = 0

    # break the piggy bank so that no money can be put into it anymore
    def smash(self):
        self.__broken = True
        self.__balance = 0

def printStatus(pigNumStr, pigNum):
    # print the amount of money in the piggy bank and whether or not it is broken
    print(pigNumStr + " has $ " + format(pigNum.balance, ".2f") + " and is", end=" ")
    if pigNum.broken:
        print("broken.")
    elif not pigNum.broken:
        print("not broken.")


def main():
    p1 = PiggyBank()
    p2 = PiggyBank()
    printStatus("p1", p1)
    p1.deposit(1.25)
    printStatus("p1", p1)
    p1.deposit(6.55)
    printStatus("p1", p1)
    p1.smash()
    printStatus("p1", p1)
    p1.deposit(2.15)
    printStatus("p1", p1)
    p1.__balance = 100.0
    p1.__broken = False
    printStatus("p1", p1)


main()
