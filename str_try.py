
#TODO:how is str implemented differently from list?

#*** str is immutable, so it can be used as dict key. 
#** thus list cannot be used as dict key. You have to use tuple. 

#* although str can be taken as a list and apply index operations and iterate on it (it should be just a sequence), 
# many opeations that can be
# applied to list doesn't apply
s = 'hello'
s[0]
for c in s:
    print c
try:
    del s[0]
except TypeError, te:
    print te.message

try:
    s.reverse()
except AttributeError, te:
    print te.message

l = list(s)
del l[0]
print 'l:', l
l.reverse()   
print 'l:', l

#** to reverse a str. Just remmeber: str can use index operation
ns = s[::-1]
print 'ns:', ns
print 's:', s


import string
print string.ascii_letters


#**** sorted() return a new sorted list, and it can be used on str (generate a list of each character). 
             # It sort by the first letter first, then the second letter.
             #
# In [79]: sorted('hello')
# Out[79]: ['e', 'h', 'l', 'l', 'o']

# In [82]: list(reversed('hello'))
# Out[82]: ['o', 'l', 'l', 'e', 'h']


#* isdigit()
s = 'oodfa870545'
l = [c for c in s if c.isdigit()]
print 'l:', l

l = filter(lambda x: x.isdigit(), s)
print 'l:', l #l is a str
print 'type(l):', type(l)


#* ord
# In [90]: ord('0')
# Out[90]: 48

# In [91]: ord('9')
# Out[91]: 57

# In [92]: ord('1')
# Out[92]: 49

# In [93]: ord('A')
# Out[93]: 65

# In [94]: ord('Z')
# Out[94]: 90

# In [95]: ord('a')
# Out[95]: 97

# In [96]: ord('z')
# Out[96]: 122

# In [97]: ord('=')
# Out[97]: 61

# In [98]: ord('!')
# Out[98]: 33

# In [99]: ord('@')
# Out[99]: 64


print 'hello'.count('l')
print 'hello'.count('o')

#split for str, extra space matters
print 'hello  world'.split(' ')
#but below is ok
print 'hello  world'.split()

#py3 style
s = 'hello {}! follw {}!'.format('world', 'me')
print(s)
#py2 style
s = 'hello %s! follow %s!' % ('China', 'you')
print s

