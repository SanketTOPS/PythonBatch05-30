class student:
    def getdata(self,stid,stnm):
        print("Student ID:",stid)
        print("Student Name:",stnm)


st=student()
#st.getdata(101,'Ashok')
id=input("Enter ID:")
name=input("Enter Name:")
st.getdata(stid=id,stnm=name)