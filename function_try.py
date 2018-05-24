

#lambda with multiple arguments, no () before :,since it is the input, and () after : since it is the return. But see the blocked blow
f = lambda x,y:(x,y+1)
print f(1,1)


#However, you cannot put multiple lines in lambda

def is_blocked(N, x, blocks):
    if x in blocks:
        return True
    if x < 1 or x > N:
        return True
    
l = [1, 2, 3, 4, 5]
bs = list(filter(lambda x:is_blocked(5, x, [3,5]), l))
print 'is blocked?:', bs

#2 dimensional
def is_blocked2(N, x, y, blocks):
    if (x, y) in blocks:
        return True
    if x < 1 or x > N:
        return True
    if y < 1 or y > N:
        return True
block_list = [(1,2), (2,3),(1,4), (0,6)]
#** need to wrap x,y around, since it is oen arg. See blow 'can accept mutiple args'
blocked = filter(lambda (x,y):is_blocked2(5, x, y, []), block_list)
print 'blocked:', list(blocked)
blocked = filter(lambda (x,y):is_blocked2(5, x, y, [(2,3)]), block_list)
print 'blocked:', list(blocked)


max(1, 9)
#** max can accept a list and return the biggest number in it
max([1,2,3,0,9])



s = ["eat", "tea", "tan", "ate", "nat", "bat"]
import collections
def anagrams(strs):
    #** use of Counter
    #** sorted turns a string into a list, but list is unhashable. So turn it into tuple
    count = collections.Counter([tuple(sorted(s)) for s in strs])
    #** use of filter, lambda. However, the result is not the type of result the problem is asking
    return filter(lambda x: count[tuple(sorted(x))]>1, strs)

print anagrams(s)   

# In [87]: filter(lambda x: x % 2==0, [1,2,3,4,5,6])
# Out[87]: [2, 4, 6]

#* why filter list below? I guess it preserve the input's type
l = filter(lambda x: x.isdigit(), s)
#the two print below have different result in python3
print 'l:', l
print 'type(l):', type(l)

t = filter(lambda x: x%2==0, (1,2,3,4)) #t will be tuple
print 't:', t

#** filter is not just a case of map and thus can always be rewritten with map. For example, below won't work.
#because it needs to produce the same number of elements of the sequence
# t2 = map(lambda x: x if x%2==0, (1,2,3,4))
#but below works
t2 = map(lambda x: x if x%2==0 else None, (1,2,3,4))
print 't2:', t2


#** map
print map(sorted, s)

print map(lambda x: x*2, [1,2,3,4])
#** map can accept mutiple args. 
print map(lambda x,y: x+y, [1,2,3,4], [1,1,1,1])


l = [1, 2, 3]
print 'Compute on each item of a list and then filter, you can use below:'
#below only work in py3
# nl = list(filter((4).__ne__, list(map(lambda x:2*x, l)))) #[2, 6]
nl2 = list(map(lambda y:y if y!=4 else 5, (map(lambda x:2*x, l)))) 
print nl2 #[2, 5, 6]
#only works in py3
# (4).__ne__

l = [{'a':1},{'b':2}]
#lambda statement's second part cannot be multiple statments. So below doesn't work. And thus many multiple lines for cannot be replaced with map, unless u wrap multiple statements into a function
# list(map(lambda item:item.update({'z':'9'});return item,  l))
def little_fun(item):
    item.update({'z':'9'})
    return item
print 'use a function to wrap multiple statements...'    
l2 = list(map(lambda item:little_fun(item),  l))
print l2

#** an inner function can be written to wrap several statements together
def seeding(field):
    def _plant_seeds(item):
        item.update({'z':'9'})
        return item
    return list(map(lambda item:_plant_seeds(item),  field))        
print 'result of seeding:', seeding([{'a':1},{'b':2}])    






#lambda without input
f = lambda:3
a = f()
print 'a:', a #3

#it needs to return stuff. Below doesn't work
# f = lambda:print("hello")
#or
# f = lambda:a=5
#but below is ok
f = lambda:1==5


cds = collections.defaultdict(f)
print cds.get(a) #None
print cds[a] #3
print cds.get(a) #3


from random import randint, choice, shuffle
print 'randint:'
print randint(0, 100)
print randint(0, 100)
print randint(0, 100)
print 'choice:'
print choice(range(10))
print choice(range(10))
print choice(range(10))
print 'shuffle:'
l = list(range(9))
shuffle(l)
print 'l:', l

print 'return nothing is return None'
def myfun():
    return

x = myfun()
print x


def less_than_7(x):
    if x < 7:
        return True
    else:
        return False


def greater_than_2(x):
    if x > 2:
        return True
    else:
        return False

l = list(range(10))
#** chaining filter
print filter(less_than_7, filter(greater_than_2, l))

print 'filter with two args'
def less_than_9(x, y):
    return x+y < 9
#** filter cannot accept multiple args    
# print filter(less_than_9, [1,2,3], [5,6,7])    
# below also doesn't work
# print filter(less_than_9, [(1,6),(2,5),(3,9)])    

def total(x, y):
    return x+y
#** reduce
print reduce(total, l) == sum(l)    
#** in py3, you need functools
import functools
print functools.reduce(total, l)



def fun(*args):
    print 'args:', args

fun(1,2)
#below is wrong
# fun(a=1,b=2) 
def fun2(*args, **kwargs):
    print 'args:', args
    print 'kwargs:', kwargs

fun2(1, 3)
fun2(a=1)    
fun2(6, b=5)


#from https://stackoverflow.com/questions/9450656/positional-argument-v-s-keyword-argument
def fn (a, b, c = 1):
    return a * b + c

print fn (1, 2)                # returns 3, positional and default.
print fn (1, 2, 3)             # returns 5, positional.
print fn (c = 5, b = 2, a = 2) # returns 9, named.
print fn (b = 2, a = 2)        # returns 5, named and default.
print fn (5, c = 2, b = 1)     # returns 7, positional and named.
print fn (8, b = 0)            # returns 1, positional, named and default.





