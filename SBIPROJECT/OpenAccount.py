#OpenAccount.py
import pickle
import numpy.random as r

from SBIexcept import validname
from validations import phonumber, acc_number, pin_number, dateofbirth, Adhaarnumber, Pannumber, mailaccount


def createaccount():
    while(True):
        try:

            with open("ramBankDetails.data", "ab") as fp:
                records = []
                print("*" * 40)
                name = validname((input("Enter customer name:")))
                dob = dateofbirth()
                adhaar =Adhaarnumber()
                pan = Pannumber()
                mail = mailaccount()
                phoneno = phonumber()
                branch=input("enter Branch name:")
                balance =500.0

                acno =acc_number()
                acpin =pin_number()
                print("*" * 40)
                print("SBI Account created successfully--verify")


                # Prepare data to store
                data =[]
                data.append(acno)
                data.append(name)
                data.append(balance)
                data.append(acpin)
                data.append(adhaar)
                data.append(pan)
                data.append((branch))

                # print("*" * 40)
                # print("customer account number:{}".format(acno))
                # print("customer name:{}".format(name))
                # print("customer pin number:{}".format(acpin))
                # print("Customer balance:{}".format(balance))
                # print("*" * 40)
                for val in data:
                    if val not in records:
                        records.append(val)
                else:
                    pickle.dump(records,fp)
                    break

        except FileNotFoundError:
            print("File does not exist.")
