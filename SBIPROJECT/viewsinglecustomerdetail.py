#viewsinglecustomerdetail.py
import pickle


import pickle
def singleaccountview():
    try:
        with open("ramBankDetails.data","rb") as fp:
            try:
                acno=int(input("Enter customer account Number to view Deatails:"))
                res=False
                while(True):
                    try:
                        record=pickle.load(fp)
                        if(acno==record[0]):
                            rec=record
                            res=True
                            break
                    except EOFError:
                        break
                if(res):
                    print("-" * 50)
                    print("\tSingle customer Deatils")
                    print("-"*50)
                    print("\tcustomer account Number={}".format(rec[0]))
                    print("\tEmployee Name={}".format(rec[1]))
                    print("\tEmployee Salary={}".format(rec[2]))
                    print("-" * 50)
                else:
                    print("\tcustomer account Number {} Does not Exist".format(acno))
            except ValueError:
                print("\tInvalid customer account Number:")
    except FileNotFoundError:
        print("File Does not Exist")
singleaccountview()

# # 40962668956			 ['krishna']			 633465			 1000.0
#  64031822871			 ['ram']			 186156			 500.0
