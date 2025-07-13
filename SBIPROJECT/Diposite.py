# Diposite.py--File Name and Module Name
import pickle

from SBIexcept import DepositError,DepositeNegativeError,DepositeAccountError,DepositeAccountNumberError
from accountvalidation import Accvalidation


def Deposite():
    records = []
    try:
        with open("ramBankDetails.data","rb") as fp:

            while(True):
                try:
                    record=pickle.load(fp)
                    records.append(record)
                except EOFError:
                    break
        res=Accvalidation()
        result=False
        for rec in records:
            if res[1]==rec[0]:
                re=rec
                result=True
                break
        if(res[0] and result==True):
            try:
                print("*"*40)
                print("Account customer Name=",re[1])
                print("Account customer number=",re[0])
                print("Present Balance=",re[-1])
                print("*"*40)
                damt=float(input("Enter deposite amount:"))
                if damt<=0:
                    raise DepositError
                else:
                    for index,j in enumerate(records):
                        if(j[0])==(res[1]):
                            records[index][3]+=damt
                            break
                    with open("ramBankDetails.data","wb") as fp:
                        for i in records:
                            pickle.dump(i,fp)
                        for index,rec in enumerate(records):
                            if(rec[0]==res[1]):
                                s=records[index][3]
                                break
                        print("-"*40)
                        print("credited amount=",damt)
                        print("aftrer deposite,present bal amount=",s)
                        print("deposite successfully complete")
                        print("-----------------------------")
            except DepositError:
                print("Deposite amount must a valid amount but not posible negitive amount")
    except ValueError:
        print("Don't enter alnums,strs and symbols--try again")






#--633465







# 40962668956