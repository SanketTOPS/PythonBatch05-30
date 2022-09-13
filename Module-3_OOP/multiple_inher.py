class nirav:
    nid=0
    nbranch=""

    def n_getdata(self):
        self.nid=input("Enter Nirav's ID:")
        self.nbranch=input("Enter Nirav's Branch:")

class ashok:
    aid=0
    abranch=""

    def a_getdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.abranch=input("Enter Ashok's Branch:")

class mitesh:
    mid=0
    mbranch=""

    def m_getdata(self):
        self.mid=input("Enter Mitesh's ID:")
        self.mbranch=input("Enter Mitesh's Branch:")

class college(nirav,ashok,mitesh):
    def allstudentdata(self):
        print("---------Nirav's Data--------")
        print("Nirav's ID:",self.nid)
        print("Nirav's Branch:",self.nbranch)
        print("---------Ashok's Data--------")
        print("Ashok's ID:",self.aid)
        print("Ashok's Branch:",self.abranch)
        print("---------Mitesh's Data--------")
        print("Mitesh's ID:",self.mid)
        print("Mitesh's Branch:",self.mbranch)


cl=college()
cl.n_getdata()
cl.a_getdata()
cl.m_getdata()
cl.allstudentdata()