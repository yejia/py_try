


#compress implementation without using izip
#TODO:if not the same length
def compress(data, selectors):
    for index,d in enumerate(data):
        if selectors[index]:
            yield d

def compress2(data, selectors):
    return [d for index,d in enumerate(data) if selectors[index]].__iter__()

# print list(compress2('ABCDEF', [1,0,1,0,1,1]))    


def count(start=0, step=1):
    while True:        
        yield start
        start += step

#TODO: why this official one uses n
def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step

# print count(10)
# print count(10)
# print count(10)        

# for i in count(10):
#      if i > 20: 
#          break
#      else:
#          print(i)


# def cycle(iterable):
#     try:
#         yield next(iterable)
#     except StopIndexError:
#                 

#TODO: below works too. But why the official implementation make a copy of the input?
def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    while True:
        for element in iterable:
            yield element
        # saved.append(element)
    # while saved:
    #     for element in saved:
    #         print 'saved:', saved
    #         yield element

print 'cycle...'
count = 0
for item in cycle('XYZ'):     
     if count > 7:
         break
     print item
     count += 1              


def dropwhile(predicate, iterable):
    iterable = iter(iterable)
    for element in iterable:
        if not predicate(element):
            yield element
            break
    for element in iterable:             
        yield element

print list(dropwhile(lambda x: x<5, [1,4,6,4,1]))        

def ifilter(predicate, iterable):
    # ifilter(lambda x: x%2, range(10)) --> 1 3 5 7 9
    return [x for x in iterable if predicate(x)]


def imap(function, *iterables):
    # imap(pow, (2,3,10), (5,2,3)) --> 32 9 1000
    for item in zip(*iterables):
        # print 'item:', item
        yield function(*item)

for item in imap(pow, (2,3,10), (5,2,3)):        
    print item

def islice(iterable, *args):
    # islice('ABCDEFG', 2) --> A B
    # islice('ABCDEFG', 2, 4) --> C D
    # islice('ABCDEFG', 2, None) --> C D E F G
    # islice('ABCDEFG', 0, None, 2) --> A C E G  
    pass


def izip3(*iterables):
    # izip('ABCD', 'xy') --> Ax By
    # iterators = map(iter, iterables)
    # while iterators:
    #     map(, iterators)

    #TODO: IndexError: string index out of range
    min_len = min([len(it) for it in iterables])
    for i in range(min_len):
        yield tuple([item[i] for item in iterables])


def izip2(*iterables):
    its = map(iter, iterables)
    # for it in its:
    while its:
        yield tuple(map(next, its))

def izip(*iterables):
    # izip('ABCD', 'xy') --> Ax By
    iterators = map(iter, iterables)
    while iterators:
        yield tuple(map(next, iterators))


for item in izip2('ABCD', 'xy'):
    print item

# def izip_longest(*args, **kwds):
#     pass


# def permutations(iterable, r=None):
#     pass

# def product(*args, **kwds):
#     # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
#     # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
#     iterables = map(iter, args)
#     for iterable in iterables:
#         yield tuple(next(iterable))

# arrays = [(-1,1), (-3,3), (-5,5)]
# cp = list(product(*arrays))
# cp        





import itertools
l = list(itertools.chain.from_iterable([[1,2],[5,6],[7,8]])) #l = [1, 2, 5, 6, 7, 8]

def izip(*iterables):
    # izip('ABCD', 'xy') --> Ax By
    its = map(iter, iterables)
    print its    
    while its:
    #*** or just use the below is the sameif its is not empty. *** while is just for catching the StopIteration. 
    #*** So instead of catch StopIteration by yourself and break, just use the while or for to catch it for you automatically. 
    #*** however, py3 seems to have deprecated this behavior. 
    # while True:
        yield tuple(map(next, its))

print list(izip('ABCD', 'xy'))


for item in  izip('ABCD', 'xy'):
    print item



# l = [1, 2, 3]
# it = iter(l)
# while it:
#     print it.next()


ll = [[1, 2, 3], [4,5]]
# it = [iter(l) for l in ll]
# while it:
#     print it[0].next()    

def f(iterables):
    its = [iter(l) for l in iterables]
    while its:
    #or just use the below is the same if its is not empty    
    # while True:
        yield its[0].next()  
        #* if not using yield, the StopIteration is raised immediately. 
        #print its[0].next()       

#generator is iterator itself. So you can put it in list(). So list() will catch the StopIteration error?
print list(f(ll))
#below will trigger the StopIteration error
# f = f(ll)
# print next(f)
# print next(f)
# print next(f)
# print next(f)


print 'iterator can be iterated only once...'
l = [1, 2, 3]
it = iter(l)
for i in it:
    print i

print 'Now nothing will show:'
for i in it:
    print i

print 'but you can get a new iterator over the iterable:'
it2 = iter(l)
for i in it2:
    print i

#** iterator's __iter__ method return self,  which means that the for-in statement will call the iterator's own next method 
print 'for statment, when used on iterable, it automatically call the iter method (.__iter__) on the iterable to get an iterator'    
for i in l:
    print i
    



print list(itertools.izip_longest('ABCD', 'xy', fillvalue='-'))        

def permutations_(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    size = r if r else len(iterable)     
    iterable = list(iterable)       
    for item in iterable:
        itc = iterable[:]
        itc.remove(item)        
        for item2 in itc: 
            itc2 = itc[:]           
            itc2.remove(item2)
            for item3 in itc2:
                yield (item, item2, item3)

# def permutations(iterable, r=None):
#     size = r if r else len(iterable)
#     item, for  for item in iterable



# print list(permutations('ABCD', 2))            
# print list(itertools.permutations('ABCD', 3))            
# print list(permutations('ABCD', 3))            



def product(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pass


def repeat(object, times=None):
    # repeat(10, 3) --> 10 10 10    
    for i in range(times):
        yield object

print list(repeat(10, 3))        


def starmap(function, iterable):
    # starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
    for it in iterable:
        yield function(*it) 

print list(starmap(pow, [(2,5), (3,2), (10,3)]))     


def takewhile(predicate, iterable):
    # takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
    for it in iterable:
        if predicate(it):
            yield it
        else:
            break 
            # or use  StopIteration  
            #raise StopIteration

print list(takewhile(lambda x: x<5, [1,4,6,4,1]))            



def tee(iterable, n=2):
    pass


#recipes.....

from itertools import *
import operator

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)


l = [1,2,3,4,5,6]

print nth(l, 2) #3
print nth(l, 1) #2
print nth(l, 6) #None
print nth(l, 5) #6
print nth(l, 6, 0) #0




def all_equal(iterable):
    "Returns True if all the elements are equal to each other"
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

print all_equal(l) #False
print all_equal('aaaaaaaaaaaaa') #True
print all_equal('aaaaaaaaaaaaab') #False


def quantify(iterable, pred=bool):
    "Count how many times the predicate is true"
    return sum(imap(pred, iterable))


print quantify(l, bool) #6
print quantify(l) #6
print quantify(l, lambda x:x>3) #3


def padnone(iterable):
    """Returns the sequence elements and then returns None indefinitely.

    Useful for emulating the behavior of the built-in map() function.
    """
    return chain(iterable, repeat(None))

p = padnone(l)
for i in range(10):
    print next(p)
#1 2 3 4 5 6 None None None None


print take(12, padnone(l)) #[1, 2, 3, 4, 5, 6, None, None, None, None, None, None]



def ncycles(iterable, n):
    "Returns the sequence elements n times"
    return chain.from_iterable(repeat(tuple(iterable), n))

print list(ncycles(l, 3)) #[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]



def dotproduct(vec1, vec2):
    return sum(imap(operator.mul, vec1, vec2))

print dotproduct([1,2,3],[4,5,6]) #32




def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)


print list(flatten([[1,2,3],[4,5,6]])) #[1, 2, 3, 4, 5, 6]


def repeatfunc(func, times=None, *args):
    """Repeat calls to func with specified arguments.

    Example:  repeatfunc(random.random)
    """
    if times is None:
        return starmap(func, repeat(args))
    return starmap(func, repeat(args, times))


print take(10, repeatfunc(random.random)) 
#something like:
# [0.23517044717398117,
#  0.3387863423216677,
#  0.21937407393806985,
#  0.8078563928893178,
#  0.39312315615449656,
#  0.708741381966231,
#  0.5094298759762235,
#  0.650845576219772,
#  0.8050691723089549,
#  0.8483819746539789]

print '2 random number btw 0 and 9'
print take(2, repeatfunc(random.randint, None, 0, 9)) #example output: [2, 5]  #times=None means keep repeating, but we only 'take' 2

print '10 random number btw 0 and 9'
print take(10, repeatfunc(random.randint, None, 0, 9)) #example output: [7, 4, 1, 5, 8, 0, 0, 0, 3, 5]

print 'can only return 2 random number btw 0 and 9 because times=2'
print take(10, repeatfunc(random.randint, 2, 0, 9))

print 'take 10 random numbers from times=12'
print take(10, repeatfunc(random.randint, 12, 0, 9))



def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

print list(pairwise('hello'))    #[('h', 'e'), ('e', 'l'), ('l', 'l'), ('l', 'o')]

 
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    #*** this is way too smart. args are a list of the same iterator. So they are all iterating on the same thing
    # everytime getting the next one. Thus izip achieve the effect this function needs.
    return izip_longest(fillvalue=fillvalue, *args)


print list(grouper('hello', 2, 'x')) # [('h', 'e'), ('l', 'l'), ('o', 'x')]

[iter('hello')]*2 #[<iterator at 0x7fb9a0449590>, <iterator at 0x7fb9a0449590>] So you see it is the same iterator



def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Recipe credited to George Sakkis
    pending = len(iterables)
    nexts = cycle(iter(it).next for it in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = cycle(islice(nexts, pending))


print list(roundrobin('ABC', 'D', 'EF')) # ['A', 'D', 'E', 'B', 'F', 'C']



#product vs permutation vs combination
#from https://docs.python.org/2/library/itertools.html
# product('ABCD', repeat=2)       AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)        AA AB AC AD BB BC BD CC CD DD

l1 = product('ABCD', repeat=2)
l2 = list(permutations('ABCD', 2))
s1 = set(l1)
s2 = set(l2)
print 'the difference btw product and permutation:'
print s1-s2 #{('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')} 
