

#** boolean can be used as 0, 1 if the situation demands (fall back). Should be pyton's mechanism to auto convert it.
# i = 1>0
# In [31]: i
# Out[31]: True

# In [32]: i - 0
# Out[32]: 1

# In [33]: i = 0

# In [34]: i = 1>0

# In [35]: i
# Out[35]: True

# In [36]: i = 0

# In [37]: i += 1>0

# In [38]: i
# Out[38]: 1



a = 2; b = 6
#*** you can do below in if. Understandable :)
if 1<a<5 and 3<b<7:
    print True
#*** so is this
if 1<a<5<b<7:
    print True

c = 3
#if we don't know if who is bigger, a or c
print 'if b is the biggest of the three'
if c<b>a: 
    print True
#or    
print 'if a is the least of the three'
if b>a<c:
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

# In [92]: 1 or 3
# Out[92]: 1

# In [93]: 1==1 or 3
# Out[93]: True

# In [94]: 3 or 1==1
# Out[94]: 3

# In [95]: 3 or 1==2
# Out[95]: 3

# In [96]: 1==2 or 3
# Out[96]: 3



#** None is smaller than any object!

class A:
    pass
a = A()
if a > None:
    print 'None is smaller than any object!'