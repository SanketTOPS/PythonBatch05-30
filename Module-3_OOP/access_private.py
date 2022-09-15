class student:
    __stid=101
    __stnm='Sanket'

    def getdata(self):
        print("Student ID:",self.__stid)
        print("Student Name:",self.__stnm)
    
    def __getsum(self,a,b):
        print("Sum:",a+b)
    
    def answer(self):
        self.__getsum(34,65)
    

st=student()
st.getdata()
st.answer()

