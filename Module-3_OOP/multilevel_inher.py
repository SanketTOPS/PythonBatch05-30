class grandfather:
    gold=0
    house=0

    def g_getdata(self):
        self.gold=input("Enter Gold details:")
        self.house=input("Enter House details:")

class father(grandfather):
    car=0
    bal=0

    def f_getdata(self):
        self.car=input("Enter Car details:")
        self.bal=input("Enter Balance details:")

class son(father):
    def printdata(self):
        print("Total Gold:",self.gold)
        print("Total House:",self.house)
        print("Total Car:",self.car)
        print("Total Balance:",self.bal)
    
sn=son()
sn.g_getdata()
sn.f_getdata()
sn.printdata()


