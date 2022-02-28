def swapFileData():
    filename=input("enter the filename1")
    filenames=input("enter the filename2")
    with open(filename,'r') as a:
        data_a=a.read()
        with open(filenames,'r') as b:
              data_b=b.read()
    with open(filenames,'w') as b:
        b.write(data_a)
    with open(filename,'w') as a:
        a.write(data_b)
swapFileData()
