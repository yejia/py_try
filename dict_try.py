



#how to add value to a dict if the key is not present. 
#*** It also show that python method can return the address (return the object itself).
#*** So for python, the passing of inputs and return are all by objects.
d = {}
d.get('a', []).append(1)
print 'd:', d
d.get('a', []).extend([2,3])
print 'd:', d
#below the defualt dict actually didn't assign the default value [] to d['a']
d['a'] = d.get('a', []).append(1)
print 'd:', d
d = {}
l = d.get('a', [])
l.append(1)
#d won't change, since l is not the same as d['a']
print 'd:', d
d['a'] = l
print 'd:', d
l2 = d['a']
if l2 is d['a']:
    print "l2 is d['a']"
l2.append(5)
print 'd:', d
l3 = d.get('a')
if l3 is d['a']:
    print "l3 is d['a']"
else:
    print "l3 is not d['a']"
l3.append(5)    
print 'd:', d
d.get('a').append(6)
print 'd:', d

d = {}
#the default value is not assigned to the d['a']
d.get('a', 2)
print 'd:', d
d['a'] = d.get('a', [])
d['a'].append(3)
print 'd:', d
d = {}
d['a'] = d.get('a', [])
d['a'].extend([5])    
print 'd:', d


#
d = {'a':1, 'b':2}
d.pop('a')
#pop and if not present,give a default instead of throw a KeyError
d.pop('c', 3)


d = {'a':1, 'b':2, 'c':3}
#*** dict can do below. How to understand the syntax below? 
#I guess it is like [i for i in xrange(10)], it gets the input from the iterator and then put inside the list constructor
#So the same, below build the input to be put inside the dict constructor, even though 'a':1 itself is not valid syntax!!!
#I guess it is just a python statement that is able to do so! In py2, iteractor kind of like string to be put together and eval.
# https://docs.quantifiedcode.com/python-anti-patterns/readability/not_using_a_dict_comprehension.html
# https://docs.python.org/3.0/whatsnew/3.0.html#overview-of-syntax-changes
#from link above, this syntax is added in py2.7, and kept in py3
d = {key:d[key] for key in d.keys() if key!='b'}
print 'd:',d


##################### helpers  #################################################

import collections

d = collections.defaultdict(list)
d['a'].append(5)
print d #  defaultdict(list, {'a': [5]})
#** use of Counter, accept seq, and count each item, return a dict
count = collections.Counter([1,2,2,3])
print 'count:', count #count: Counter({2: 2, 1: 1, 3: 1})


#* defaultdict takes a function
#** lambda without an arg
cds = collections.defaultdict(lambda:3)
print cds.get(1) #None
print cds[1] #3
print cds.get(1) #3

collections.OrderedDict