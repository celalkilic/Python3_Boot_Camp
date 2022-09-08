"""Variable Assignment

Rules for variable names

- names can not start with a number
- names can not contain spaces, use _ intead
- names can not contain any of these symbols:

    :'",<>/?|\!@#%^&*~-+

--it's considered best practice (PEP8) that names are lowercase with underscores
avoid using Python built-in keywords like list and str
--avoid using the single characters l (lowercase letter el),
--O (uppercase letter oh) and I (uppercase letter eye) as
they can be confused with 1 and 0

Dynamic Typing

Python uses dynamic typing, meaning you can reassign variables
to different data types.
This makes Python very flexible in assigning data types;
it differs from other languages that are statically typed."""

my_dogs = 2
print(my_dogs)

my_dogs = ['Samy', 'Frankie']
print(my_dogs)

#Assigning variables
a = 5
print(a)
a = 10
print(a)
print(a + a)

#Reassingning variables

a = a + 10
print(a)

a += 10
print(a)

a *= 2
print(a)

#to learn what kind of data you are using
type(a)
print(type(a))