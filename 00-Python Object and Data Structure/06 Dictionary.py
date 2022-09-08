"""Dictionaries

We've been learning about sequences in Python but now we're going
to switch gears and learn about mappings in Python. If you're familiar
with other languages you can think of these Dictionaries as hash tables.
This section will serve as a brief introduction to dictionaries
and consist of:

1.) Constructing a Dictionary
2.) Accessing objects from a dictionary
3.) Nesting Dictionaries
4.) Basic Dictionary Methods

So what are mappings? Mappings are a collection of objects that are stored
by a key, unlike a sequence that stored objects by their relative position.
This is an important distinction, since mappings won't retain order since they
have objects defined by a key.
A Python dictionary consists of a key and then an associated value. That value
can be almost any Python object."""

#Constructing a Dictionary

#Make a dictionary with {} and : to signify a key and a value

my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict)
print(my_dict['key2'])

my_dict = {'key1': 123, 'key2': [12,23,34], 'key3':['item0', 'item1', 'item2']}
print(my_dict['key3'])
print(my_dict['key2'])
print(my_dict.keys())
print(my_dict.get('key2'))

#call an index on that value
print(my_dict['key3'][1])

#Can then even call methods on that value
print(my_dict['key3'][0].upper())

print(my_dict['key1'])

#Subtract 123 from the value
my_dict['key1'] = my_dict['key1'] - 123
print(my_dict['key1'])

#Create a new Dictionary
d = {}

#Create a new key through assignment
d['animal'] = 'dog'

#Can do this with any object
d['answer'] = 42

print(d)

#Nested dictionary
d = {'key1': {'nestedKey': {'subnestkey': 'value'}}}
print(d['key1']['nestedKey']['subnestkey'])

d = {'key1': 1, 'key2': 2, 'key3': 3}

#Methods

#keys is a method to return a list of all keys
print(d.keys())

#value is method to grab all values
print(d.values())

#items is a method to return tuples of items
print(d.items())