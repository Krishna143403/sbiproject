#Program Opening the File in read mode
#FileOpenEx2.py
try:
    fp=open("kvr1.data","r")
except FileNotFoundError:
    print("File Does not Exist")
else:
    print("Type of fp=", type(fp))
    print("File Opened in Read Mode Sucessfully ")
finally:
    print("---------finally-----------")
    try:
        print("Is File Closed before close()=",fp.closed)
        #close the File Manually
        fp.close()
        print("Is File Closed after close()=", fp.closed)
    except NameError:
        print("File Not yet Opened-No Need to Close")