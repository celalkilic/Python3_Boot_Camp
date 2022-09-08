#accept any three strings from one input() call
"""str1, str2,str3 = input("enter three strings....").split()
print(str1, str2, str3)"""
#find differences
set1 = {10,20,30}
set2 = {20, 40,50}
set1.difference_update(set2)
print(set1)

#add a list of elements to given set

sample_set = {'yellow', 'orange', 'black'}
sample_listadd = ['blue', 'green', 'red']
sample_set.update(sample_listadd)
print(sample_set)
