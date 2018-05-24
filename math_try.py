



max(1, 9)
#** max can accept a list and return the biggest number in it
max([1,2,3,0,9])




result = 67
r = -result
print r
print -result


#largest float number
print float('inf')
#smallest float number
print float('-inf')   
import sys
print sys.maxint
print - sys.maxint - 1
#if over the limit, it is auto converted to long. And in python, the size of long is unlimited (There is no explicitly defined limit. The amount of available address space forms a practical limit.)
print - sys.maxint - 20
print sys.maxsize
print 2**32
print 2**64
print 2**63
#for py3, maxsize is used.

#None is smaller than anything
print None < sys.maxint
print None < - sys.maxint - 1
print None < float('inf')
print None < float('-inf')



print int(0x7fe554708e18) 
print hex(140622940900888) #0x7fe554708e18
print hash(0x7fe554708e18) #140622940900888
print hash(140622940900888) #140622940900888
print 0x7fe554708e18 == 140622940900888 #True
print int(0x7fe554708e18) == hex(140622940900888) #False. one is int, the other is str
print type(0x7fe554708e18) #int
print type(140622940900888) # int
print type(int(0x7fe554708e18)) #int
print type(hex(140622940900888)) #str
print hash(int(0x7fe554708e18))
print hash(hex(140622940900888))



import random
#random.randint can pass range
print 'random number btw 0 and 5:', random.randint(0, 5)

print random.choice([4, 8, 3, 9 ,0])


# #*** max int in python:2**31-1, min -2**31    
# #** use max and min together to get value in btw    
# return max(-2**31, min(sign * ret,2**31-1))

