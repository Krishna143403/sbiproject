#Project.py---Main program

from Diposite import Deposite
from OpenAccount import createaccount
from SBIMenu import menu
from fundsTransfer import FundsTransferAmount
from searchaccount import Singleaccount
from selectallrecords import allrecords

from withdraw import WithDrawamount

while(True):
    menu()

    ch=input("Enter Ur Choice:")
    match(ch):
        case"1":
           createaccount()
        case "2":
            Deposite()
        case "3":
            WithDrawamount()
        case "4":
            Singleaccount()
        case "5":pass
        case "6":
            allrecords()
        case "7":
            FundsTransferAmount()
        case "8":
            print("thx for using project")
            break
        case _:
            print("\tUR Selection of Operation is Wrong-try again")


