#Progrram for Reading employee values from key board and same them as record in file
# by using Pickling Process.
#EmpPickEx1.py
import pickle
def saveemprecord():
    with open("emp.pick","ab") as fp:
        while(True):
            #Read emp values from Key Board
            print("--------------------------------------")
            empno=int(input("Enter Employee Number:"))
            empname=input("Enter Employee Name:")
            empsal=float(input("Enter Employee Salary:"))
            print("--------------------------------------")
            #create an empty list and place emp values
            lst=[]
            lst.append(empno)
            lst.append(empname)
            lst.append(empsal)
            #save Iterable object data lst into file by using dump()
            pickle.dump(lst,fp)
            print("Employee Data Saved in File Sucessfully")
            print("--------------------------------------")
            ch=input("Do u want insert another Record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for using this program")
                break

#Main Program
saveemprecord() # Function Call
