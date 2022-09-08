class student:
    stid=23
    stnm='Mitesh'

    def getdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)

# Object of Class
"""st=student()
st.getdata()
st.stid=45
st.stnm='Sanket'
st.getdata()"""

# Instance of Class
student().getdata()
student().stid=3
student().stnm='Pratik'
student().getdata()
