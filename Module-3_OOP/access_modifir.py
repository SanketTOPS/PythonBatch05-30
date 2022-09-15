class student:
    __stid=12
    __stnm='Hitesh'

    def __getsum(self,a,b):
        print("Sum:",a+b)

st=student()
#print(st.stid)
#print(st.stnm)
st.getsum(34,65)