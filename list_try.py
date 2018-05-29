
#*** list is mutable, thus list cannot be used as dict key. You have to use tuple. 



###################### Python's notion of object ######################################


#* python's function calling is passing by reference (called passing by object in python), return also return the reference
def m(l):
    l.append(5)
    return l

l = [0]
l2 = m(l)
l #[0, 5]
l2 #[0,5]
l == l2 #True
l is l2 #True





#remove a tuple from a list
l = [(1,2), (3,5), (2,6), (5,3), (3,5)]
l.remove((3,5))     
print 'l after remove:', l
# l after remove: [(1, 2), (2, 6), (5, 3), (3, 5)]
del l[0]
print 'l after del:', l
# l after del: [(2, 6), (5, 3), (3, 5)]

#list slicing get a copy, instead of working on the original one
l = [1,2,3,4,5]
l1 = l[:2]
print 'l1:', l1
l1[1] = 7
print 'l1:', l1
print 'l:', l



print 'Demonstrating value passing in for loop...'
l = [1,2,3,4,5]
#below len(l) is only evaluated once in the for loop. So although len(l) is changed, it doesn't affect the for loop
for i in xrange(len(l)):
    l.append(1)
    print i
print 'l:', l   


print 'Demonstrating value passing in for loop, when value is an object...'
#for loop get the next item from iterator, which generate from the list, which is modifed in the loop
#Generally, avoid modifying the seq while iterating
l = [1,2,3,4,5]
for i in l:
    if i < 3:
        l.append(6)
    print i
print 'l:', l    

#removing item while iterating, dangerous
l = [1,2,3,4,5]
for item in l:
    print item
    if item == 2:
        l.remove(item)
print 'l:', l
#appending while iterating, seems ok as long as you are not always appending
#But in general, it is best not to change a list while iteating over it
l = [1,2,3,4,5]
for item in l:
    print item
    if item == 4:
        l.append(9)    
print 'l:', l


           
#*** in practice, just make a copy of the list for iterating if you need to modify the original list during the loop
l = [1,2,3,4,5]
for item in l[:]:
    print item
    if item == 2:
        l.remove(item) 
print 'l:', l  



############################# basic list operations  #######################################################

l = [('a', 1), ('c', 6), ('b', 2)]
#** you can unpack the tubple of the list directly in for loop. With enumrate, it is the same mechanism.
for c, i in l:
    print c, i
#*** it can also unpacked like below. The mechanism is just "keep unpacking unpacked"
for index, (c, i) in enumerate(l):
    print index, c, i


#you can unpack a tuple, or a list
x,y = (1,2)
print x
print y
#below works as well
x,y = 1,2
print x
print y


#* + used for list, but it is different from list.extend since it doesn't modify the first
print [1,2] + [3,4]
l = [1, 2]
l + [3,4]
print 'l:', l





l = [1,2,3,4]
#** the right side index, not inclusive
print 'l[:-1]:', l[:-1]
#** left side index, inclusive
print 'l[1:]:', l[1:]


#** tuple turn a list into a tuple. It accepts list as input, and turn it into a tuple
#*** you need use tuple as the dict key, not list  
# In [83]: t = tuple([1,2,3])
# In [84]: t
# Out[84]: (1, 2, 3)


############## list comprehension ####################

l = [[1, 2, 3], [4, 5, 6]]
#*** two for list comprehension
l1 = [i for sublist in l for i in sublist]
l2 = [i for sublist in l for i in sublist if i % 2 == 1]
print 'l:', l
print 'l1:', l1
print 'l2:', l2
#*** each for statement can have its "if"
l3 = [i for sublist in l if 2 in sublist for i in sublist if i % 2 == 1]
print 'l3:', l3
l4 = [i for sublist in l if not 2 in sublist for i in sublist if i % 2 == 1]
print 'l4:', l4

d = {'a':[2,4,5,7],'b':[0,1,8,9, 11, 12]}
#** take the first 3 items from each value. Below value didn't appear in the 2nd for statement, 
# and value[i] uses the two defined variable for computation/composition
#*** the item can come from both the frist for and the second for
l1 = [value[i] for value in d.values() for i in xrange(3)]
print 'l1:', l1
#*** each for statement can have its "if"
l2 = [value[i] for value in d.values() if len(value)>4 for i in xrange(3)]
print 'l2:', l2






#normally list's operation work on the list's end. To remove item from the beginning, you can 
#get the value of the first item, then remove that value. Or you can reverse first, then pop.
l = [1,2,3,4,5]
del l[0] #list.__delitem__
del l[2]
#better than using index and then remove

# In [6]: l = [1, 2, 3]

# In [7]: l
# Out[7]: [1, 2, 3]

# In [8]: l[0]
# Out[8]: 1

# In [9]: l.remove(1)

# In [10]: l
# Out[10]: [2, 3]

#* for list to work on the left end, you can use insert to add
#l.insert(0, val)

#to have constant time working on the left side, use deque


######################   list used as stack or queue ########################################
# for stack, you can just use list. For queue, deque is the officially recommended one, since
# it has the popleft method. 

from collections import deque
s = deque([])
#** you should be able to use a lot like a list
if s:
    print 'stack is not empty!'
else:
    print 'stack is empty!'  
s.append(1)  
if s:
    print 'stack is not empty!'
else:
    print 'stack is empty!' 
print 's[0]:', s[0]    
s.append(2)
s.append(5)
print 's:', s
s[1] = 8  
print 's:', s
x = s.pop()
print 'x:', x
print 's:', s
y = s.popleft()
print 'y:', y
print 's:', s
s.append(9)
print 'after appendleft:'
s.appendleft(100)
print s

l = list(s)
print 'l:', l
l2 = [s]
print 'l2:', l2
print l.append(7)
print l


######################### builtin functions that can be applied to list and their usages #################################################################

l = [3,2,5]
#sorted return a new sorted list. I guess guido think the default should be not changing the original list
sorted(l)
print 'l is still not sorted:', l
l = sorted(l)
print 'l:', l
#**** or you can do it in place. See below
l[:] = sorted(l)
#but you can surely use list's own sort method
l = [5, 6, 1]
l.sort()
print 'l:', l
l.reverse()
print 'l:', l
#but below get AttributeError
try:
    l.sort().reverse()
except AttributeError, ae:
    print ae.message  




# In [71]: l
# Out[71]: []

#*** you can use reversed (which returns an iterator), and apply to an in-place list memory space
# In [72]: l[:] = reversed([1,2,3])

# In [73]: l
# Out[73]: [3, 2, 1]

# In [74]: l[:] = [5,6,7]

# In [75]: l
# Out[75]: [5, 6, 7]

#* but if you do below, you only get an iterator
# In [76]: l = reversed([1,2,3])

# In [77]: l
# Out[77]: <listreverseiterator at 0x7feb6a95f9d0>


# In [65]: s_l
# Out[65]: ['e', 'u', 'l', 'b', ' ', 's', 'i', ' ', 'y', 'k', 's', ' ', 'e', 'h', 't']

# #** reverse a slice of a list doesn't work
# In [67]: s_l[:4].reverse()

# In [68]: s_l
# Out[68]: ['e', 'u', 'l', 'b', ' ', 's', 'i', ' ', 'y', 'k', 's', ' ', 'e', 'h', 't']

# #** but you can use reversed and assign to the memory space.
# This should be easy to understand, if you think of operation like s_l[3] = 'c', it also change the list in place. Just expand it to slice, or the whole.
# In [69]: s_l[:4] = reversed(s_l[:4])

# In [70]: s_l
# Out[70]: ['b', 'l', 'u', 'e', ' ', 's', 'i', ' ', 'y', 'k', 's', ' ', 'e', 'h', 't']





m = [[1,0,0,0],
     [0,1,1,0],
     [1,0,0,1]]

#*** zip
print zip(m)
 # [([1, 0, 0, 0],), ([0, 1, 1, 0],), ([1, 0, 0, 1],)]

# In [17]: 

# In [17]: 
# #*** be aware of * so that the seq is used as positional argument for the zip function
# In [17]: zip(*m)
# Out[17]: [(1, 0, 1), (0, 1, 0), (0, 1, 0), (0, 0, 1)]

# In [18]: m = [[1,0,0,0],
#               [0,1,1,0],
#               [1,0,0]]
# #** if not the same length, extra items are discarded.
# In [19]: zip(*m)
# Out[19]: [(1, 0, 1), (0, 1, 0), (0, 1, 0)]





max(1, 9)
#** max can accept a list and return the biggest number in it
max([1,2,3,0,9])

import random
#random.randint can pass range
print 'random number btw 0 and 5:', random.randint(0, 5)

print random.choice([4, 8, 3, 9 ,0])


 #*** loop  through a 2d array(list)    
m = [[1,0,0,0],
      [0,1,1,0],
      [1,0,0,1]]
l = [m[i][j] for i in range(len(m)) for j in range(len(m[i]))]
print 'looping through matrix:', l

# list[::-1] reverse the list

m1 = [[3,5,7,9],
     [2,1,0,4],
     [6,8,7,1]
    ]
#rotate a matrix 90 degree clockwise
m1[:] = zip(*m1[::-1])
print 'after turnning 90 degree clockwise:', m1
m2 = [[3,5,7,9],
     [2,1,0,4],
     [6,8,7,1]
    ]
m2[:] = zip(*[sublist[::-1] for sublist in m2])
print 'after turnning 90 degree counter clockwise:', m2

m3 = [[3,5,7,9],
     [2,1,0,4],
     [6,8,7,1]
    ]
#turn the tuple in the list back into list    
m3[:] = map(list, zip(*m3[::-1]))
print 'after turnning 90 degree clockwise:', m3



#*** only work for 0 index
# n * m matrix convert to an array => matrix[x][y] => a[x * m + y]
# an array convert to n * m matrix => a[x] =>matrix[x / m][x % m];

#***  only work for 0 index
# int mid = (begin + end) / 2;
# int mid_value = matrix[mid/col_num][mid%col_num];


l = [1,2,3,4,5,6,7,8]
l2 = l[::2]
print 'l2:', l2
for index, n in enumerate(l[::2]):
  print index, n
print 'l:', l






#if items of a sequence is list or tuple, it can be sorted first on the first item then the second...
l1 = [[2,3,6], [1,3], [6,8,9],[9,1,2]]
l1.sort()
l1 # [[1, 3], [2, 3, 6], [6, 8, 9], [9, 1, 2]]
t1 = [(2,3,6), (1,3), (6,8,9),(9,1,2)]
t1.sort() 
t1 #[(1, 3), (2, 3, 6), (6, 8, 9), (9, 1, 2)]



import itertools
l = list(itertools.chain.from_iterable([[1,2],[5,6],[7,8]])) #l = [1, 2, 5, 6, 7, 8]
