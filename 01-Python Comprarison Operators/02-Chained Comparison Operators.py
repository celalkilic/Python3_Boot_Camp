"""Chained Comparison Operators

An interesting feature of Python is the ability to chain multiple comparisons
to perform a more complex test. You can use these chained comparisons as shorthand for larger Boolean
Expressions.
In this lecture we will learn how to chain comparison operators and we will also
introduce two other important statements in Python: and and or."""

#Chained Comparison Operators

print(1 < 2 < 3)

# and

print(1 < 2 and 2 < 3)

print(1 < 3 > 2)

print(1 < 3 and 3 > 2)

# or

print(1 == 2 or 2 < 3)

print(1 == 1 or 100 == 1)

print(1 < 2 and 2 < 1)