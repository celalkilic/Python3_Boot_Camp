"""Files Read and Write

Python uses file objects to interact with external files on your computer.
These file objects can be any sort of file you have on your computer, whether it be an audio
file, a text file, emails, Excel documents, etc.
Note: You will probably need to install
certain libraries or modules to interact with those various file types, but they are
easily available. (We will cover downloading modules later on in the course).
Python has a built-in open function that allows us to open and play with basic
file types.

 "r" read
 "a" append
 "w" write
 "x" create
 open() open file to operate any function"""
import os

#File Handling

#Open a file

#open() function
path = "C:/Users/zeyne/Desktop/celal/demo.txt"

demo = open(path)
#print(demo.read())

#demo = open(path, "r")
#print(demo.read())

#readline()
#print(demo.readline())
#print(demo.readline())

#readlines
#print(demo.readlines())

#Loop concept

'''
demo = open(path, "r")
for x in demo:
    print(x)
'''
# close()
'''
demo = open(path, "r")
print(demo.read())
demo.close()
'''

#append "a"
# write "w"

#demo = open(path, "a")
#demo.write("\nThis is new line in my file...!")
#demo.close()
#Open and read the file after appending
#demo = open(path, "r")
#print(demo.read())


#Delete file
#os.remove(path2)

''' 
if os.path.exists(path2):
    os.remove()
else:
    print("The file does not exist")
'''
#os.remove(path)
#os.rmdir("/Users/bobit/Desktop/pythonFiles")