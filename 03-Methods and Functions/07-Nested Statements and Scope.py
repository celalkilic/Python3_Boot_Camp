"""Nested Statements and Scope

Now that we have gone over writing our own functions, it's important to understand how
Python deals with the variable names you assign. When you create a variable name in Python
the name is stored in a name-space. Variable names also have a scope, the scope determines
the visibility of that variable name to other parts of your code.

This idea of scope in your code is very important to understand in order to properly assign
and call variable names.

In simple terms, the idea of scope can be described by 3 general rules:

Name assignments will create or change local names by default.

Name references search (at most) four scopes, these are:
local
enclosing functions
global
built-in
Names declared in global and nonlocal statements map assigned names to enclosing module and function scopes.
The statement in #2 above can be defined by the LEGB rule.


LEGB Rule:

L: Local — Names assigned in any way within a function (def or lambda), and not declared global
   in that function.
E: Enclosing function locals — Names in the local scope of any and all enclosing functions
   (def or lambda), from inner to outer.
G: Global (module) — Names assigned at the top-level of a module file, or declared global
   in a def within the file.
B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,..."""

# Nested Statements and Scope

x = 25  # global


def printer():
    x = 50  # local variable
    return x


print(x)
print(printer())

'''
LEGB Rule:
L: Local — Names assigned in any way within a function (def or lambda), and not declared global
   in that function.
E: Enclosing function locals — Names in the local scope of any and all enclosing functions
   (def or lambda), from inner to outer.
G: Global (module) — Names assigned at the top-level of a module file, or declared global
   in a def within the file.
B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...
'''

name = "this is a global name"


def greet():
    name = 'Sammy'

    # Enclosing function (inner method)
    def hello():
        print('Hello ' + name)

    hello()


greet()

# global
print(name)

# Built in
print(len(name))

# local variables

x = 50  # global


def func(x):
    print('x is ', x)
    x = 2  # local
    print('Changed local x to ', x)


func(x)
print('x is still ', x)