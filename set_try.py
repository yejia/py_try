



# In [107]: s = set([2,3,1,2])

# In [108]: s
# Out[108]: {1, 2, 3}

# In [109]: s1 = {2,3,6}


#** you still can iterate and even enumerate on set. However, the order is not garanteed
# In [111]: for i in s:
#    .....:     print i
#    .....:     
# 1
# 2
# 3

# In [112]: for index,i in enumerate(s):
#    .....:     print index, i
#    .....:     
# 0 1
# 1 2
# 2 3

# In [113]: s2 = {8,5,9}

# In [114]: for i in s2:
#    .....:     print i
#    .....:     
# 8
# 9
# 5

# In [115]: for i in s2:
#              print i
#    .....:     
# 8
# 9
# 5

# In [116]: s2
# Out[116]: {5, 8, 9}


#** set operations
s1 = set([1, 2, 3])
s2 = set([3, 4, 5])
print 's1 | s2'
print s1 | s2
print 's1:', s1
print 's2:', s2
print 's1 & s2'
print s1 & s2
print 's1.intersection(s2):'
print s1.intersection(s2) #the same as &
print 's1:', s1
print 's2', s2
print 's1.union(s2)'
print s1.union(s2) #the same as |
print 's1:', s1
print 's2', s2
print 's1 - s2'
print s1 - s2
print 's1:', s1
print 's2', s2
#set cannot be applied to +
try:
    print s1 + s2
except TypeError as te:
    print te.message    

#** also set has no index operation
try:
    print s1[0]
except TypeError as te:
    print te.message  

