"""Numbers

We'll learn about the following topics:
1.) Types of Numbers in Python
2.) Basic Arithmetic
3.) Differences between classic division and floor division
4.) Object Assignment in Python

Types of numbers

Python has various "types" of numbers (numeric literals). We'll mainly focus on integers and
floating point numbers.
Integers are just whole numbers, positive or negative. For example: 2 and -2 are examples of integers.
Floating point numbers in Python are notable because they have a decimal point in them,
or use an exponential (e) to define the number. For example 2.0 and -2.1 are examples
of floating point numbers. 4E2 (4 times 10 to the power of 2) is also an example of
a floating point number in Python.
In this tutorial we will be mainly working with integers or simple float number types.

Here is two main types we will spend most of our time working with some examples:
Examples	                 Number "Type"
1,2,-5,1000	                 Integers
1.2,-0.5,2e2,3E2	         Floating-point numbers
"""
#Basic Arithmatic

#Addition
print('Addition: ', 7+4)
#Subtraction
print('Subtraction: ', 7-4)
#Multiplication
print('Multiplication: ', 7*4)
#Divison
print('Division: ', 7/4)
#Floor Division
print('Floor Division: ', 7//4)
#Modulo
print('Modulo: ', 7%4)

#powers
print(2**3) # 2* 2* 2= 8

# can also do roots this way
print(4**0.5)

#Order of operations in Python
print(2 + 10 * 10 + 3) #105

#Can use parenthesis to specify orders
print((2+10)*(10+3)) #156

#Variable Assignments
a = 5
print(a+a)
a = 10
a = a + a
print(a)

#Example
my_income = 100
tax_rate = 0.2
my_taxes = my_income*tax_rate
print(my_taxes)