#withdraw.py
import pickle
from accountvalidation import Accvalidation
from SBIexcept import WithDrawError
def WithDrawamount():

    try:
        with open("ramBankDetails.data","rb") as fp:
            records = []
            while(True):
                try:
                    record=pickle.load(fp)
                    records.append(record)
                except EOFError:
                    break
        res = Accvalidation()
        result = False
        for rec in records:
            if res[1] == rec[0]:
                re = rec
                result = True
                break
        if (res[0] and result == True):
            try:
                print("*" * 40)
                print("Account customer Name=", re[1])
                print("Account customer number=", re[0])
                print("Present Balance=", re[-1])
                print("*" * 40)
                damt = float(input("Enter deposite amount:"))
                if damt <= 0:
                    raise WithDrawError
                else:
                    for index, j in enumerate(records):
                        if (j[0]) == (res[1]):
                            records[index][3] -= damt
                            break
                    with open("ramBankDetails.data", "wb") as fp:
                        for i in records:
                            pickle.dump(i, fp)
                        for index, rec in enumerate(records):
                            if (rec[0] == res[1]):
                                s = records[index][3]
                                break
                        print("-" * 40)
                        print("credited amount=", damt)
                        print("aftrer deposite,present bal amount=", s)
                        print("deposite successfully complete")
                        print("-----------------------------")
            except WithDrawError:
                print("Deposite amount must a valid amount but not posible negitive amount")
    except ValueError:
        print("Don't enter alnums,strs and symbols--try again")














    except FileNotFoundError:
        print("File Does not Exist--try again")
    # try:
    #     print(records)
    #     acno=int(input("Enter Customer Account no:"))
    #     wamt=int(input("Enter ur Withdraw Amount:"))
    #     pin=int(input("Enter Ur pin no:"))
    #
    # except WithDrawError:
    #     print("Ur account no does not match--try again")
    #
    # res=False
    # while (True):
    #
    #     for record in records:
    #         if acno ==record[0]:
    #             if pin==record[2]:
    #
    #                 record[3]-=wamt
    #                 print("Ur account {} debited with INR:{}".format(acno,wamt))
    #                 res=True
    #                 break
    #
    #     if(res):
    #         print("Account no does not exist")
    #         with open("D:\\ProjectSBI.data","wb") as fp:
    #             for record in records:
    #                 pickle.dump(record,fp)
    #
    #
