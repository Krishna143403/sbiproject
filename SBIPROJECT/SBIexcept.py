#SBIExcept.py---file name and module name
class DepositError(Exception):pass
class WithDrawError(BaseException):pass
class InSuffFundError(Exception):pass
class InvalidNameError(BaseException):pass
class SpaceError(Exception):pass
class ZeroNameLengthError(Exception):pass
class SpaceNameError(Exception):pass
class AcnSpaceError(Exception):pass
class PhoneNumberError(Exception):pass
class PhoneNumberLengthError(Exception):pass
class AccountNumberError(Exception):pass
class AccountNumberLengthError(Exception):pass
class PinError(Exception):pass
class PinLengthError(Exception):pass
class DobError(Exception):pass
class AdhaarError(Exception):pass
class AdhaarNumberError(Exception):pass
class PanError(Exception):pass
class PanSpaceError(Exception):pass
class MailError(Exception):pass
class MailSpaceError(Exception):pass
class PhoneSpaceError(Exception):pass
class DepositeAmountError(Exception):pass
class DepositeNegativeError(Exception):pass
class DepositeAccountError(Exception):pass
class DepositeAccountNumberError(Exception):pass
class AccNumberError(Exception):pass
class AccountNumError(Exception):pass
class AccountlenthError(Exception):pass
class PINNumberError(Exception):pass
class PINlenthError(Exception):pass
class AccountNumError(Exception):pass
class ACSPACEERROR(Exception):pass
class PINSPACEERROR(Exception):pass
class EnterAccNumberError(Exception):pass
class RecAccError(Exception):pass
class NegativeError(Exception):pass
class WithDrawError(Exception):pass

#RecAccError,NegativeError,WithDrawError



def validname(accname):
    while(True):
        try:
            if(len(accname)==0):
                raise  SpaceNameError
            else:
                acname=accname
                if(len(acname)==0):
                    raise AcnSpaceError
                else:
                    res=False
                    for i in acname:
                        if(not i.isalpha()):
                            res=True
                            break
                    if(res==True):
                        raise  NameError


                    else:
                        return acname
        except SpaceNameError:
            print("Don't enter space u must enter valid name--try again")
        except AcnSpaceError:
            print("ur selection name is wrong--try again")
        except NameError:
            print("Don't enter alnums,strs and symbolss--try again")