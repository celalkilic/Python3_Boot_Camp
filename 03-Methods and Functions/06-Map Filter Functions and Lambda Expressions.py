"""Lambda Expressions, Map, and Filter

Now its time to quickly learn about two built in functions, filter and map. Once we learn about
how these operate, we can learn about the lambda expression, which will come in handy when you
begin to develop your skills further!

map function

The map function allows you to "map" a function to an iterable object. That is to say you can
quickly call the same function to every item in an iterable, such as a list.

filter function

The filter function returns an iterator yielding those items of iterable for which function(item)
is true. Meaning you need to filter by a function that returns either True or False.
Then passing that into filter (along with your iterable) and you will get back only the
results that would return True when passed to the function.

lambda expression

One of Pythons most useful (and for beginners, confusing) tools is the lambda expression.
Lambda expressions allow us to create "anonymous" functions. This basically means we can quickly
make ad-hoc functions without needing to properly define a function using def.

Function objects returned by running lambda expressions work exactly the same as those created
and assigned by defs. There is key difference that makes lambda useful in specialized roles:
lambda's body is a single expression, not a block of statements.

The lambda's body is similar to what we would put in a def body's return statement.
We simply type the result as an expression instead of explicitly returning it.
Because it is limited to an expression, a lambda is less general that a def.
We can only squeeze design, to limit program nesting. lambda is designed for coding simple functions,
and def handles the larger tasks."""

# map filter and lambda expressions

# map function

def square(num):
    return num**2
my_nums = [1,2,3,4,5]

print(map(square,my_nums))

#loop concept with map
for item in map(square, my_nums):
    print(item)
#List concept with map
print(list(map(square, my_nums)))

def splicer(myString):
    if len(myString) % 2 == 0:
        return 'even'
    else:
        return myString[0]
myNames = ['John', 'Cindy', 'Sarah', 'Kelly', 'Mike']
print(list(map(splicer, myNames)))

# filter function
def check_even(num):
    return num % 2 == 0
nums = [0,1,2,3,4,5,6,7,8,9,10]

print(filter(check_even, nums))
#list concept with filter
print(list(filter(check_even, nums)))

#loop concept with filter
for n in filter(check_even, nums):
    print(n)

# lambda expression

#square = lambda num : num**2

print(list(map(lambda num : num ** 2, nums)))

print(list(filter(lambda n: n % 2 == 0, nums)))

print(list(map(lambda x: x[0], myNames)))