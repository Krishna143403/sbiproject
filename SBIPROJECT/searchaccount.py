# searchaccount.py
import pickle
def Singleaccount():

    try:
        with open("ramBankDetails.data","rb") as fp:
            try:
                acno=int(input("ENter Account no:"))
                res=False
                while(True):
                    try:
                        record=pickle.load(fp)
                        if(acno==record[0]):
                            res=True
                            break
                    except EOFError:
                        break
                if(res):
                    print("Account no {} exist--valid account no".format(acno))
                else:
                    print("Account no {} does not exist--Invalid account no".format(acno))
            except ValueError:
                print("\tInvalid Account Number")
    except FileNotFoundError:
        print("File does not Exist")
