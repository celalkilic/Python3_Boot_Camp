#tuple
#tuple is similar to a list
#we can not change the elments of tuple once it is assigned
#creating a tuple
first_tuple = (1,2,3,4)
print(type(first_tuple))
print(first_tuple)
#mixed data type
second_tuple = (1,2,'hello',5,6)
print(second_tuple)
#you can creat a tuple without pranthesis
first_tuple = 3,4,5, 'ilhan', 'k'
print(first_tuple)
print(type(first_tuple))
#in tuple , having one element without paramthesis is not enough. to fix this issue use comma
first_tuple = ('hello')
print(type(first_tuple))
first_tuple = ('hello',)
print(type(first_tuple))
#accessing tuple
second_tuple = ('p', 'e', 'r','m','i')
print(second_tuple[0])
print(second_tuple[3])
#matrix tuple
third_tuple = ([1,2,3],[4,5,6],[7,8,9])
print(third_tuple)
print(third_tuple[0][0])
print(third_tuple[1][1])
print(third_tuple[2][2])
#negative indexing
print(third_tuple[-2][-1])
#slicing
slicing_tuple = ('c','e','l','a','l')
print(slicing_tuple[1:2])
print(slicing_tuple[:3])
#can not any element tuple is created once
#slicing_tuple[0] = 'm' does not support item assignment

#count item
print(slicing_tuple.count('a'))
#index
print(slicing_tuple.index('a'))
#membership
print('a' in slicing_tuple)
print('m' in slicing_tuple)
#iterating
for name in ('celal','zeynep'):
    print('hello', name)