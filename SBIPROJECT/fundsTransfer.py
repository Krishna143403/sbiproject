import pickle
from SBIexcept import PinError,RecAccError,NegativeError,WithDrawError
from accountvalidation import  Accvalidation
def FundsTransferAmount():
    records = list()
    try:
        with open("ramBankDetails.data", "rb") as fp:
            while True:
                try:
                    record= pickle.load(fp)
                    records.append(record)
                except EOFError:
                    break

        res = Accvalidation()
        result=False
        for rec in records:
            if (res[1] == rec[0] and res[2] == rec[2]):
                re = rec
                result=True
                break

        # if (not result):
        #     raise Acc_NumberError
        if(not res[0] ):
            raise PinError

        print("----" * 30)
        print("\tAccount number=", re[0])
        print("\tAccount holder Name=", re[1])
        print("\tPresent balance=", re[-1])
        print("---" * 30)
        print("\t\tEnter Ur fund Transfering Account details")
        recno = int(input("Enter Funds transferable Account number:"))
        receiver = False
        receiver_account=None
        for rec in records:
            if (recno == rec[0]):
                receive_record = rec
                receiver = True
                break
        if (not receiver):
            raise RecAccError

        print("---" * 30)
        print("\tFund recever Account number=", receive_record[0])
        print("\tFunds recever Name=", receive_record[1])
        print("---" * 30)
        amt = float(input("Enter Transfering  Amount:"))

        if (amt <= 0):
            raise NegativeError
        if ((re[3] < amt + 500)):
            raise WithDrawError
        for index, rec in enumerate(records):
            if (rec[0]) == (re[0]):
                records[index][3]-=amt
                break
        for index, rec in enumerate(records):
            if (rec[0]) == (receive_record[0]):
                records[index][3]+=amt
                break
        with open("ramBankDetails.data","wb") as fp:
            for i in records:
                pickle.dump(i, fp)
            for index, rec in enumerate(records):
                if (rec[0]) == (re[0]):
                    g=records[index][3]
                    break
            for index, rec in enumerate(records):
                if (rec[0]) == (receive_record[0]):
                    r=records[index][3]
                    break

            print("---"*30)
            print("\tAcno '{}' Present Balance Amount Giver={}".format(res[1], g))
            print("\tAcno '{}' Present Balance Amount receiver={}".format(recno, r))

        print("\n\tFunds Transfer Transcation Successfully completed..!")
        print("---"*30)


    except ValueError:
        print("\tDont enter str,symbols,alnums in withdraw")
    except NegativeError:
        print("\tDont try negative value amount withdraw")
    except WithDrawError:
        print("\tNot have suficent funds in ur account")
    except FileNotFoundError:
        print("\tFile Not Eixst")
    except PinError:
        print("\tAccount or Pin Invalid")
    # except Acc_NumberError:
    #     print("Account number incorrect")
    except RecAccError:
        print("\tRecever Account Detais Invalid")


# # 40962668956			 ['krishna']			 633465			 1000.0
#  64031822871			 ['ram']			 186156			 500.0
# ****************************************