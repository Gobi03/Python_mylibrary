def add(x, y):
    ans = x + y
    return ans
n = add(3, 5)
print n             #=> 8

def func():
    return 3, "ABC"
n, s = func()
print n, s               #=> 3 ABC

# lambda expression
myfunc = lambda x, y: x + y
print myfunc(3, 5)                 #=> 8
