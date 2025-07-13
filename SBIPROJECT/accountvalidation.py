from SBIexcept import AccNumberError,AccountNumError,EnterAccNumberError,AccountlenthError,PINNumberError,PINlenthError,AccountNumError,ACSPACEERROR,PINSPACEERROR
import pickle
def Accvalidation():
    try:
        with open("ramBankDetails.data", "rb") as fp:
            try:
                acno = input("Enter Account number:")
                if (not acno.isdigit()):
                    raise EnterAccNumberError
                if (len(acno) != 11):
                    raise AccountlenthError
                if(len(acno)==0):
                    raise ACSPACEERROR
                acno = int(acno)

                acpin = input("Enter pin number:")
                if (not acpin.isdigit()):
                    raise PINNumberError
                if (len(acpin) != 6):
                    raise PINlenthError
                if(len(acpin)==0):
                    raise PINSPACEERROR
                acpin = int(acpin)
            except EnterAccNumberError:
                print("\tDont enter str,symbols,alnums in account number")
                return False, None, None

            except AccountlenthError:
                print("\tU Must Enter 10 digit Account number only")
                return False, None, None
            except ACSPACEERROR:
                print("\tU must Enter Account,Dont enter space")
            except PINSPACEERROR:
                print("U must Enter ur Pin not space")
            except PINNumberError:
                print("\tDont Enter Str,Symbols,Alnus in PIN NUMBER")
                return False, None, None
            except PINlenthError:
                print("\tU must Enter 6 digit pin only")
                return False, None, None
            res = False
            while True:
                try:
                    r = pickle.load(fp)
                    if (acno == r[0] and acpin == r[2]):
                        rec = r
                        res = True
                        break
                except EOFError:
                    break
            if not res:
                raise AccNumberError

            else:
                print("---"*30)
                print("\t\t Account is Existing ")
                print("---"*50)
                return res, acno, acpin
    except AccNumberError:
        print("\tAccount Numbere or Pin Invalid")
        return False, None, None
    except FileNotFoundError:
        print("\tFile Not Eixst")
        return False, None, None
