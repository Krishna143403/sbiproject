#Program Opening the File in read mode
#FileOpenEx5.py
try:
    with open("kvr1.data","r+") as fp:
        print("-----------------------------------------------")
        print("Type of fp=", type(fp))
        print("File Opened in Read+ Mode Sucessfully ")
        print("Is File Closed within 'with open() as' Block=",fp.closed)
        print("---------File pointer Properties----------------")
        print("\tFile Name=",fp.name)
        print("\tFile Mode=", fp.mode)
        print("\tIs File Readable=",fp.readable())
        print("\tIs File Writable=", fp.writable())
        print("-----------------------------------------------")
    print("\nIs File Closed after 'with open() as' Block=",fp.closed)

except FileNotFoundError:
    print("File Does not Exist")