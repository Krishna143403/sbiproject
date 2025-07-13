from SBIexcept import PhoneNumberError, PhoneNumberLengthError, SpaceError,AccountNumberError,AccountNumberLengthError,PinError,PinLengthError,DobError,AdhaarError,AdhaarNumberError,PanError,PanSpaceError,MailError,MailSpaceError,PhoneSpaceError
import random as r

def phonumber():
    while (True):
        try:
            phoneno=input("Enter customer phone number:")

            if len(phoneno)!=10:
                raise PhoneNumberLengthError
            else:
               for i in phoneno:
                   if not i.isdigit():
                       raise PhoneNumberError
                   else:
                       phoneno=int(phoneno)
                   return phoneno


            # if (len(phoneno) == 10):
            #     raise PhoneNumberLengthError
            # else:
            #     res=False
            #     for v in phoneno:
            #         if not v.isdigit():
            #             res=True
            #             break
            #     if(res):
            #         break
            #     else:
            #         if(len(phoneno)==0):
            #             raise PhoneSpaceError
            #
            #
            #
            #         else:
            #             phoneno=int(phoneno)
            # return phoneno
        except PhoneNumberLengthError:
            print("u Must enter a valid phone number")
        except PhoneNumberError:
            print("Don't Enter alnums,str and symbols--try again")
        except ValueError:
            print("Don't Enter space Ur enter a valid number")


def acc_number():
    # try:

            acno=r.randint(10**10,10**11-1)
            return acno
    #         if len(str(acno))!=10:
    #             raise AccountNumberError
    #         res=False
    #         for k in acno:
    #             if(len(k)==9):
    #                 res=True
    #                 break
    #         if(res):
    #                 raise AccountNumberLengthError
    #
    #         else:
    #             if acno==0:
    #                 raise SpaceError
    #         return acno
    # except AccountNumberError:
    #     print("U must enter Valid Account Number--try again")
    # except AccountNumberLengthError:
    #     print("Don't enter strs,alnums and symbols--try again")
    # except SpaceError:
    #     print("Don't enter space u must enter account number")


def pin_number():
    while(True):
        try:
            acpin=r.randint(100000,1000000-1)
            res=False
            for j in str(acpin):
                if(j==5):
                    res=True
                break
            if(res):
                raise PinError
            else:
                if(acpin==0):
                    raise PinLengthError
            return int(acpin)
        except PinError:
            print("Don't enter alnums,strs and symbols--try again")
        except PinLengthError:
            print("Don't enter space u must enter pin number")

def dateofbirth():
    while(True):
        try:
            dob=input("Enter customer data of birth:")
            res=False
            for i in dob:

                if dob.isalnum():
                    res=True
                    break
            if(res):
                raise DobError
            return dob
        except DobError:
            print("Don't enter space u must enter ur dob")


def Adhaarnumber():
    while(True):
        try:
            adhaar=input("Enter customer adhaar number:")
            if not adhaar.isdigit():
                raise AdhaarError
            else:
                if len(adhaar)<=11:
                    raise AdhaarNumberError
                else:
                    adhaar=int(adhaar)
            return adhaar
        except AdhaarError:
            print("don't enter alnums,strs and Symbols--try again")
        except AdhaarNumberError:
            print("U must enter 12 digit adhaar number")


def Pannumber():
    while(True):
        try:
            pannumber=input("Enter customer PAN Number:").upper()
            res=False
            for i in pannumber:
                if not i.isalnum():
                    res=True
                    break
            if(res):
                raise PanError

            else:
                if pannumber==0:
                    raise PanSpaceError
            return pannumber
        except PanError:
            print("don't enter alphabets and symbols--try again")
        except PanSpaceError:
            print("Don't enter space u must enter valid pan number")

def mailaccount():
    while(True):
        try:
            Gmail=input("Enter customer Mail Account:")
            res=False
            for x in Gmail:
                if not x.isalnum():
                    re=True
                    break
            if(res):
                    raise MailError

            else:
                if Gmail==0:
                    raise MailSpaceError
            return Gmail
        except MailError:
            print("Don't enter digits--try again")
        except MailSpaceError:
            print("Don't enter space for mail u must enter valid mail")
