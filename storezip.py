from zipfile import ZipFile

# Read the file to binary and return the binary
# file should be a single zip file opened in 'rb', which means "read binary"
def filetobinary(file):
    bin = file.read()
    return bin

# Take the binary and output the file location of the unzipped files
def binarytofiles(binary):
    filename = 'output.zip' #temp file to write binary to. this will be unzipped
    with open(filename, 'wb') as file:
        file.write(binary) #write binary to file

    with ZipFile(filename, 'r') as zip:
        zip.extractall('temp') #unzip the file into a folder named 'temp'
        names = zip.namelist() #get the folder name

    return f'temp/{names[0]}' #return the directory of the unzipped files
