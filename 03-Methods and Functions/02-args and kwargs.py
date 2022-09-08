"""*args and **kwargs in Python

*args

The special syntax *args in function definitions in python is used to pass a variable
number of arguments to a function. It is used to pass a non-keyworded, variable-length argument list.

The syntax is to use the symbol * to take in a variable number of arguments; by convention,
it is often used with the word args.
What *args allows you to do is take in more arguments than the number of formal arguments that
you previously defined. With *args, any number of extra arguments can be tacked on to your current
formal parameters (including zero extra arguments).
For example : we want to make a multiply function that takes any number of arguments and able to
multiply them all together. It can be done using *args.
Using the *, the variable that we associate with the * becomes an iterable meaning you can do
things like iterate over it, run some higher order functions such as map and filter, etc.

**kwargs

The special syntax **kwargs in function definitions in python is used to pass a keyworded,
variable-length argument list. We use the name kwargs with the double star.
The reason is because the double star allows us to pass through keyword arguments (and any number of them).

A keyword argument is where you provide a name to the variable as you pass it into the function.
One can think of the kwargs as being a dictionary that maps each keyword to the value
that we pass alongside it. That is why when we iterate over the kwargs there doesn’t seem
to be any order in which they were printed out."""


# args and kwargs
def myfunc(a, b):
    return sum((a, b)) * .05


result = myfunc(40, 60)
print(result)


def myfunc(a=0, b=0, c=0, d=0):
    return sum((a, b, c, d)) * .05


result2 = myfunc(40, 60, 20)
print(result2)


# *args
# When a function parameter starts with an asterisk it allows for an arbitrary number of arguments,
# and the function takes them in as a tuple of values

def myfunc(*args):
    return sum(args) * .05


result3 = myfunc(40, 60, 20)
print(result3)


def myfunc(*spam):
    return sum(spam) * .05


result4 = myfunc(40, 60, 20)
print(result4)


# **kwargs
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(f"my favorite fruit is {kwargs['fruit']}")
    else:
        print("I don't like fruit")


myfunc(fruit='pineapple')
myfunc()


# *args and **kwargs

def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"i like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"may I have some {kwargs['juice']} juice?")
    else:
        pass


myfunc('eggs', 'spam', fruit='cherries', juice='orange')


def printScores(player, *args):
    print(f"player name :  {player}")
    for i in args:
        print(i)


printScores('john', 20, 40, 30, 80, 90, 70)


# crate a fubction which takes multiple arguments and sum them up

def sum(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print(f"sum of numbers is {sum}")


sum(20, 30, 40, 50, 60, 80, 90, 100)


def information(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} is {v}")


information(firstName="celal", lastName="kilicarslan", age=25, phone=1234567899)
def petName(ownerName, **kwargs):
    print("owner name :", ownerName)
    for k,v in kwargs.items():
        print(f"{k} :", v)
petName("celal", dog = "snowball", fish = "dory", cat = "balla")