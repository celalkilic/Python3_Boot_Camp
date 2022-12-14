"""if, elif, else Statements

if Statements in Python allows us to tell the computer to perform alternative
actions based on a certain set of results.

Verbally, we can imagine we are telling the computer:
"Hey if this case happens, perform some action"

We can then expand the idea further with elif and else statements, which allow us to tell the computer:
"Hey if this case happens, perform some action. Else, if another case happens, perform
some other action. Else, if none of the above cases happened, perform this action."
Let's go ahead and look at the syntax format for if statements to get a better idea of this:

if case1:
    perform action1
elif case2:
    perform action2
else:
    perform action3"""
#if elif and else

#First Example

if True:
    print('it was true!')

#Second example
x = False

if x:
    print('x was True!')
else:
    print('i will be printed in any case where x is not true')

#Third Example
loc = 'Bank'

if loc == 'Auto Shop':
    print("Welcome to the Auto shop")
elif loc == 'Bank':
    print('Welcome to the bank')
else:
    print('Where are you?')

#Fourth Example
person = 'Sammy'

if person == 'Sammy':
    print('Welcome Sammy!')
else:
    print('Welcome, what is your name?')

#Fifth Example

person = 'George'

if person == 'Sammy':
    print('Welcome Sammy')
elif person == 'George':
    print('Welcome, George!')
else:
    print('Welcome, what is your name?')