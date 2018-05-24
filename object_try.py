


#python's function calling is passing by reference (called passing by object in python), return also return the reference
def m(l):
    l.append(5)
    return l

l = [0]
l2 = m(l)
l #[0, 5]
l2 #[0,5]
l == l2 #True
l is l2 #True



#This is to show syntaxically you can write like below, which might be helpful when writing on whiteboard
if 1==1: x = 1
else: x = 2

print 'x:', x


print 'Demonstrating value passing in for loop...'
l = [1,2,3,4,5]
#below len(l) is only evaluated once in the for loop. So although len(l) is changed, it doesn't affect the for loop
for i in xrange(len(l)):
    l.append(1)
    print i
print 'l:', l   


print 'Demonstrating value passing in for loop, when value is an object...'
#for loop get the next item from iterator, which generate from the list, which is modifed in the loop
l = [1,2,3,4,5]
for i in l:
    if i < 3:
        l.append(6)
    print i
print 'l:', l    




# from LinkedList import Linked_List
# ll = Linked_List()
# ll.add_node(5)
# ll.add_node(5)
# if ll.tail == ll.head:
#     print 'It is comparing the value although no __eq__ defined'
# else:
#     print 'It is comparing the identity'   

#It is comparing the identity




class A:

    class B:
        def __init__(self):
            pass
        
        def __str__(self):
             return 'I am B!'

    class _C:
        def __init__(self):
            pass
        
        def __str__(self):
             return 'I am C!'      

    class __D:
        def __init__(self):
            pass
        
        def __str__(self):
             return 'I am D!'            


    def __init__(self):
        self.field1 = 'foo'
        self._field2 = 'bar'
        self.__field3 = 'too'
a = A()

print 'a.field1:', a.field1
print 'a._field2:', a._field2
#however, __field3 cannot be accessed
# print 'a.__field3:', a.__field3

#B,and _C is accessible from outside
b = A.B()
print 'b:', b
c = A._C()
print 'c:', c
#__D is not accessible
# d = A.__D()






#how to add value to a dict if the key is not present. 
#*** It also show that python method can return the address (return the object itself).
#*** So for python, the passing of inputs and return are all by objects.
d = {}
d.get('a', []).append(1)
print 'd:', d #{}
d.get('a', []).extend([2,3])
print 'd:', d #{}
#below the defualt dict actually didn't assign the default value [] to d['a']
d['a'] = d.get('a', []).append(1)
print 'd:', d #{'a': None}
d = {}
l = d.get('a', [])
l.append(1)
#d won't change, since l is not the same as d['a']
print 'd:', d #{}
d['a'] = l
print 'd:', d #{'a': [1]}
l2 = d['a']
if l2 is d['a']:
    print "l2 is d['a']" #will print
l2.append(5)
print 'd:', d #{'a': [1, 5]}
l3 = d.get('a')
if l3 is d['a']:
    print "l3 is d['a']" #print this one
else:
    print "l3 is not d['a']"
l3.append(5)    
print 'd:', d #d: {'a': [1, 5, 5]}
d.get('a').append(6)
print 'd:', d  #d: {'a': [1, 5, 5, 6]}

d = {}
#the default value is not assigned to the d['a']
d.get('a', 2)
print 'd:', d #{}
d['a'] = d.get('a', [])
d['a'].append(3)
print 'd:', d #d: {'a': [3]}
d = {}
d['a'] = d.get('a', [])
d['a'].extend([5])    
print 'd:', d #d: {'a': [5]}



class A:
    pass

class B:
    pass

a = A()
b = B()
l = [(a, b), (b, a), (a, a), (b, b)]
#*** below is using identiy to find the tuple to remove, I think
l.remove((b, a))
print 'l:', l


d = {a:1, b:2}
# no __hash__ (not __eq__) overriding, it should be using the object as the key, which we can look at as the identity
print 'd[a]:', d[a]

print 'a:', a
print 'hash(a):', hash(a)
print 'id(a):', id(a)
print 'hex(id(a)) should be the same as address of a:', hex(id(a))

#So how is the hash defined??TODO:


class A:
    def __init__(self, val):
        self.val = val

    def __eq__(self, theother):
        if self.val == theother.val:
            return True
        else:
            return False    

#class A defined __eq__, but not __hash__

a = A(3)
b = A(3)
c = A(5)

try:
    hash(a)
except TypeError as te:
    print te.message    

# since a,b,c cannot be hashed, they cannot be used in set and dict's keys
s = set()
try:    
    s.add(a)
except TypeError as te:
    print te.message
d = {}
try:    
    d[a] = 1
except TypeError as te:
    print te.message

#although a cannot be hashed, it still can be used in list. It will use its __eq__ to match

l = [(a, b), (b, a), (a, a), (b, b), (a, c)]
print 'l:', l
#*** if __eq__ method is implemented, it will remove according to value is equal
l.remove((b, a))
print 'l:', l
l.remove((b, a))
print 'l:', l
l.remove((b, a))
print 'l:', l
l.remove((b, a))
print 'l:', l
print 'len(l):', len(l)
try:
    l.remove((b, a))
except ValueError, ve:
    print ve.message
print 'l:', l
print 'len(l):', len(l)  




l = [3,2,5]
#sorted return a new sorted list. I guess guido think the default should be not changing the original list
sorted(l)
print 'l:', l
l = sorted(l)
print 'l:', l
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




#** one is smaller than any object!

class A:
    pass
a = A()
if a > None:
    print 'None is smaller than any object!'




class A:
    def __init__(self, val):
        self.val = val
        self.next = None

    def push(self):
        pass

    
    def pop(self):
        pass

a = A(2)
d = a.__dict__
print 'a:', a                
print 'dir(a):', dir(a)
d['val'] = 5
print 'a.val:', a.val
print 'd.val:', d['val']
d2 = vars(a)
print 'd2:', d2
print 'type(d2):', type(d2)




class MyClass(object):
    my_classfield = []

    @classmethod
    def myclassmethod(cls, val):
        print 'received ', val

    def regular_method(self):
        #** you reference the class full name instead of cls, which is only available in classmethod
        MyClass.myclassmethod(5)

myclass = MyClass()
myclass.regular_method()     


#if accessible
class A:
    class __B:
        pass
#not accessible
# A.__B
class A:
    class _B:
        pass
#accessible
A._B           

class A:
    __x = 1
#not accessible
# A.__x
class A:
    _x = 1
#accessible
print A._x

class A:
    __x__ = 1
#accessible
print A.__x__  

class A:
    class __B__:
        pass
#accessible
A.__B__  

class A:
    def __method(self):
        pass
a = A()
#not accessible
# a.__method()
class A:
    def __method__(self):
        pass
a = A()
#accessible
a.__method__()
class A:
    def _method(self):
        pass
a = A()
#accessible
a._method()


# l1 = [1]
# In [8]: isinstance(l1, list)
# Out[8]: True

# In [9]: isinstance(l1, object)
# Out[9]: True

# In [10]: isinstance(type, object)
# Out[10]: True

# In [11]: isinstance(l1, type)
# Out[11]: False

# In [12]: isinstance(list, type)
# Out[12]: True




from functools import wraps

class attr_block_meta(type):
    def __new__(meta, cname, bases, dctry):
        def _setattr(self, name, value):
            if not hasattr(self, name):
                raise AttributeError("'" + name + "' not an attibute of " + cname + " object.")
            object.__setattr__(self, name, value)

        def override_setattr_after(fn):
            @wraps(fn)
            def _wrapper(*args, **kwargs):
                cls.__setattr__ = object.__setattr__
                fn(*args, **kwargs)
                cls.__setattr__ = _setattr
            return _wrapper

        cls = type.__new__(meta, cname, bases, dctry)
        cls.__init__ = override_setattr_after(cls.__init__)
        return cls


class ImPoint(object):
    __metaclass__ = attr_block_meta
    def __init__(self, q, z):
        self.q = q
        self.z = z

point = ImPoint(1, 2)
print point.q, point.z
point.w = 3  # Raises AttributeError