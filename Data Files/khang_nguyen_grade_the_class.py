def openFile(file_name):
    try:
        with open(file_name,'r'):
            print ('Successfully opened class1.txt' + str(file_name))
    except IOError:
        print ('File cannot be found.')
        
filename = input("Enter a filename: ")
openFile(filename)