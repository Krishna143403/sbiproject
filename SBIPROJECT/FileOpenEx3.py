#Program Opening the File in read mode
#FileOpenEx3.py
try:
    with open("kvr1.data","r") as fp:
        print("Type of fp=", type(fp))
        print("File Opened in Read Mode Sucessfully ")
        print("Is File Closed within 'with open() as' Block=",fp.closed)
    print("\nIs File Closed after 'with open() as' Block=",fp.closed)
except FileNotFoundError:
    print("File Does not Exist")