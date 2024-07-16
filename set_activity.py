#activities from string
#pop: removes last element
#remove: removes particular element
#Discard: removes particular key
'''
a={45,4-5j,(4),4.5}
a.pop()
a.remove(4-5j)
a.discard(4.5)
print(a)
'''
#Difference: returns uncommon keys as new set.
# Symmetric difference: Uncommon keys from both set.

'''
set_1 = {'a', (4, ), 45, 4.4, 3-4j, False, 'a'}

set_2 = {'a', 'b', 'c' }

set_3 = {14.5, 4+5j, 'kiwi', (4,5) , (45, ) }
print (set_2. difference (set_1))
print (set_2. symmetric_difference(set_1))
'''
#3.
'''
a={'apple', 'orange', 'grapes'}
a.add ({'kiwi'})
print(a)
print(a[1])
'''

#We cant add set inside set, because it is mutable.
#We cant do indexing because sets are unordered
#4.
s1 = {1,2,3, 4,5,6} 
s1.ada ([10,20])
s1.add ((25,40))
print(s1)
