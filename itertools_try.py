


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