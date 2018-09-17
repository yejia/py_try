

from os import system, name
import pprint
from time import sleep

#static print, or step print
def sprint(*args):
    #**** way to dig into the exact steps of the algorithm            
    # for windows
    if name == 'nt':
        system('cls')         
    # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')                            
    pp = pprint.PrettyPrinter(indent=2)
    for arg in args:
        pp.pprint(arg)
    sleep(0.3)           
    


l1 = 10
l2 = 8
dp = [[0 for _ in xrange(l2)] for _ in xrange(l1)]
count = 0
for i in xrange(1, l1):
    for j in xrange(1, l2):
        count += 1
        dp[i][j] = count
        # for windows
        if name == 'nt':
            system('cls')         
        # for mac and linux(here, os.name is 'posix')
        else:
            system('clear')                            
        pp = pprint.PrettyPrinter(indent=1)
        print('l1:',l1)
        print('l2:',l2)        
        pp.pprint(dp)
        sleep(2)


