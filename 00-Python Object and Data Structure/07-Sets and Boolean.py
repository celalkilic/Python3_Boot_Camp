"""Sets
Sets are an unordered collection of unique elements.
We can construct them by using the set() function.

Booleans
Python comes with Booleans (with predefined True and False displays that are basically just the integers 1 and 0).
It also has a placeholder object called None."""
#order and index not important
first_set = {'java','python', 'groovy'}
print(first_set)
#check is java is present in set or not
print('java' in first_set)
#change item == you can not change element once a set is created
#add element
first_set.add('html')
print(first_set)
#update function
first_set.update(['javascript','c++','ruby'])
print(first_set)
#size
print(len(first_set))
#remove
first_set.remove('javascript')
print(first_set)
#pop==remove last item
first_set.pop()
print(first_set)
#join two sets
second_set = {'eclipse', 'anaconda'}
thitd_set = second_set.union(first_set)
print(thitd_set)
#for loop
for x in first_set:
    print(x)
#Create a list
x = set()

x.add(1)
print(x)

x.add(2)
print(x)

#unique
x.add(1)
print(x)

list1= [1,1,2,2,3,4,5,6,1,1]
print(set(list1))
print(list1)

#Booleans

a= True
print(a)

print(1>2)

b = None
print(b)

my_file = open('/Users/bobit/Desktop/test.txt')
my_file.read()