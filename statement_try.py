


a = 2; b = 6
#*** you can do below in if. Understandable :)
if 1<a<5 and 3<b<7:
    print True
#*** so is this
if 1<a<5<b<7:
    print True

c = 3
#if we don't know if who is bigger, a or c:
if c<b>a:
    print True

print 'the assicative of boolean operator'
if not 1==1 or 3==3:
    print True    
#above is the same as:
if (not 1==1) or (3==3):
    print True        
#but different from:
if not (1==1 or 3==3):
    print True       
else:
    print False


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

#you can unpack a tuple
x,y = (1,2)
print x
print y
#below works as well
x,y = 1,2
print x
print y

#try except block
print 'No specifying what error:'
d = {}
try:
    x = d['a']
except:
    print 'Error getting value!'

print 'specify what error:'
d = {}
try:
    x = d['a']
except KeyError:
    print 'KeyError!'

print 'specify what error and try to get more info from it:'
d = {}
try:
    x = d['a']
except KeyError as ke:
    print 'KeyError:', ke.message   

#try except else. Just try the statement that need to be tried, put the rest into else.
d = {'a':1}
try:
    x = d['a']
except KeyError as ke:
    print 'KeyError:', ke.message       
else:
    y = x
    print 'y is computed:', y    


#errors:
IndexError # list, tuple index,
TypeError  #
AttributeError 
ValueError

# raise IndexError
# raise IndexError('No such index!')
# raise Exception('something wrong')
# raise


#***
a = 1 if l else 2
print 'a:', a
#above statement is not only for assignment, can be used for all one line statement
print True if True else False
l = [1,2,3]
l.append(5) if len(l)==2 else l.remove(1)
print 'l:', l


n = 6
#*** going by step -1, the first argument is inclusive, and the second is not
for i in range(n-1,-1,-1):
    print i


#** None is smaller than any object!

class A:
    pass
a = A()
if a > None:
    print 'None is smaller than any object!'






l = [[1, 2, 3], [4, 5, 6]]
#*** two for list comprehension. Below sublist appear after it is defined in the first for statement
l1 = [i for sublist in l for i in sublist]
l2 = [i for sublist in l for i in sublist if i % 2 == 1]
print 'l:', l
print 'l1:', l1
print 'l2:', l2

d = {'a':[2,4,5,7],'b':[0,1,8,9, 11, 12]}
#** take the first 3 items from each value. Below value didn't appear in the 2nd for statement, 
# and value[i] uses the two defined variable for computation/composition
l1 = [value[i] for value in d.values() for i in xrange(3)]
print 'l1:', l1
#*** each for statement can have its "if"
l2 = [value[i] for value in d.values() if len(value)>4 for i in xrange(3)]
print 'l2:', l2



#** ~ : ~x =  -x - 1
# In [26]: i = 0

# In [27]: ~i
# Out[27]: -1

# In [28]: ~i
# Out[28]: -1

# In [29]: i
# Out[29]: 0

# In [30]: j = 4

# In [31]: ~j
# Out[31]: -5

# In [32]: i = -6

# In [33]: ~i
# Out[33]: 5



#with statement
# with open("x.txt") as f:
#     data = f.read()
    



# In [1]: import operator

# In [2]: operator.or_
# Out[2]: <function operator.or_>

# In [3]: operator.or_?
# Type:        builtin_function_or_method
# String form: <built-in function or_>
# Docstring:   or_(a, b) -- Same as a | b.

# In [4]: reduce
# Out[4]: <function reduce>

# In [5]: reduce(operator.or_, [1,2,3])
# Out[5]: 3


# In [7]: reduce(operator.or_, [0,2,3,0])
# Out[7]: 3

# In [8]: reduce(operator.and_, [0,2,3,0])
# Out[8]: 0


dir(operator)


def get_int():
    for i in xrange(100):
        yield i
intg = get_int()
while True:
    i = intg.next()
    print i
    if i > 10:        
        break


class Bank:
    crisis = False
    def create_atm(self):
        while not self.crisis:
            yield '$100'

hsbc = Bank()
corner_street_atm = hsbc.create_atm()
print(corner_street_atm.next())            
print(corner_street_atm.next())            
print([corner_street_atm.next() for cash in range(5)])



#from https://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists
#** for else statement.
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        # loop fell through without finding a factor
        print n, 'is a prime number'