import random as r
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
