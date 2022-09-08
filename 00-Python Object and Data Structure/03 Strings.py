"""Strings

Strings are used in Python to record text information, such as names.
Strings in Python are actually a sequence, which basically means
Python keeps track of every element in the string as a sequence.
For example, Python understands the string "hello' to be a sequence of letters
in a specific order. This means we will be able to use indexing
to grab particular letters (like the first letter, or the last letter).
This idea of a sequence is an important one in Python and
we will touch upon it later on in the future.

We'll learn about the following:
1.) Creating Strings
2.) Printing Strings
3.) String Indexing and Slicing
4.) String Properties
5.) String Methods
6.) Print Formatting"""

#To create a String in Python we can use '' or ""

print('hello')
print("hello")

#Entire phrase
print("This is also String in Python")
print('This is also String in Python')

#Be Careful
print("I'm using single quotes")

#Define string variable
name = "ilhan"
print(name)
print(type(name))

print('use \n to print a new line')

s = 'hello world'
print(s)

#Show first element
print(s[0])

print(s[2])

#We can use a : to perform slicing which grabs everything up to a designated point

print(s[3:])
print(s[:3])
print(s[:])
print(s[:-1])
print(s[::1])
print(s[::2])

#We can use this to print a string backwards - reverse string
print(s[::-1])

#Concatenate

b = 'hello world'

b = b + ' concatenate me!'
print(b)

print('Addition: ', (2+1))

letter = 'z'
print(letter*10)

#Uppercase

m = 'my name is Ilhan'
print(m.upper())

#lowercase
print(m.lower())

#Split- split a string by blank space
print(m.split())

#split by a specific element
print(m.split('n'))

# .format()

print('Insert another string with curly brackets: {}'.format('The inserted string'))
print('My First name is ilhan and last name is: {}'.format('turkmen'))

#placeholders method %s
print("I'm going to inject %s here"%'something')

print("I'm going to inject %s text here, and %s text here."%('some', 'more'))

x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here."%(x, y))

#Format conversion methods

print('He said his name was %s'%'Frank')
print('He said his name was %r'%'Frank')

# \t
print('I once caught a fish %s'% 'this \tbig')
print('I once caught a fish %r'% 'this big')

# %s and %d
print('I wrote %s programs today'%3.75)
print('I wrote %d programs today'%3.75)

#Padding and precision of floating point numbers
print('Floating point numbers: %5.2f'%(13.144))
print('Floating point numbers: %5.0f'%(13.144))
print('Floating point numbers: %5.3f'%(13.144))