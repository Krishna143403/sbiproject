import pickle
def allrecords():
    with open("ramBankDetails.data","rb") as fp:
        print("*"*40)
        print("All customer Details")
        print("*" * 40)
        print("ACC_NUMBER\t\t\t\tCUST_NAME\t\t\tPIN_NO\t\t\tBalance_Amount")
        while(True):
            try:
                rec=pickle.load(fp)
                for val in rec:
                    print("",val,end="\t\t\t")
                print()
            except EOFError:
                break
