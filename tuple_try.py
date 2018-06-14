


#from https://stackoverflow.com/questions/101268/hidden-features-of-python?page=2&tab=votes#tab-top
# tuple unpacking in python 3

# in python 3, you can use a syntax identical to optional arguments in function definition for tuple unpacking:

# >>> first,second,*rest = (1,2,3,4,5,6,7,8)
# >>> first
# 1
# >>> second
# 2
# >>> rest
# [3, 4, 5, 6, 7, 8]
# but a feature less known and more powerful allows you to have an unknown number of elements in the middle of the list:

# >>> first,*rest,last = (1,2,3,4,5,6,7,8)
# >>> first
# 1
# >>> rest
# [2, 3, 4, 5, 6, 7]
# >>> last
# 8



# >>> (a, (b, c), d) = [(1, 2), (3, 4), (5, 6)]
# >>> a
# (1, 2)
# >>> b
# 3
# >>> c, d
# (4, (5, 6))