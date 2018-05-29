


from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print p.x
 # 1
print p.y
# 2

Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(0,0,1)
print c.x
print c.y
print c.r

from collections import deque
q = deque(['a', 'b', 'c'])
q.append('m')
q.appendleft('n')
print q
print q.pop()
print q.popleft()
print q



#defaultdict #find in others





from collections import OrderedDict
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
# in the order it is inserted
print od.keys() #['z', 'y', 'x'] 
# OrderedDict.popitem(last=True) #The popitem() method for ordered dictionaries returns and removes a (key, value) pair. The pairs are returned in LIFO order if last is true or FIFO order if false.

#from https://docs.python.org/2/library/collections.html
# >>> # regular unsorted dictionary
# >>> d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# >>> # dictionary sorted by key
# >>> OrderedDict(sorted(d.items(), key=lambda t: t[0]))
# OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

# >>> # dictionary sorted by value
# >>> OrderedDict(sorted(d.items(), key=lambda t: t[1]))
# OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])

# >>> # dictionary sorted by length of the key string
# >>> OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
# OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])



from collections import Counter