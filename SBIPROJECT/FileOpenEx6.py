#Program Opening the File in Write mode
#FileOpenEx6.py
with open("kvr2.data","a") as fp:
    print("-----------------------------------------------")
    print("Type of fp=", type(fp))
    print("File Opened in Write Mode Sucessfully ")
    print("Is File Closed within 'with open() as' Block=",fp.closed)
    print("---------File pointer Properties----------------")
    print("\tFile Name=",fp.name)
    print("\tFile Mode=", fp.mode)
    print("\tIs File Readable=",fp.readable())
    print("\tIs File Writable=", fp.writable())
    print("-----------------------------------------------")
print("\nIs File Closed after 'with open() as' Block=",fp.closed)
