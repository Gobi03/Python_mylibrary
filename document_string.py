# ドキュメントストリング(__doc__)

mymod.py

"""A sample module"""
class MyClass:
    """A sample class"""
    def myfunc(self, x, y):
        """A sample function"""
        return x + y

mytest.py

import mymod
print mymod.__doc__                  #=> A sample module
print mymod.MyClass.__doc__          #=> A sample class
print mymod.MyClass.myfunc.__doc__   #=> A sample function



# 対話式の場合 help() でも参照されます。
$ python
>>> import mymod
>>> help(mymod)
Help on module mymod:

NAME
    mymod - A sample module

FILE
    /root/mymod.py

CLASSES
    MyClass

    class MyClass
     |  A sample class
     |
     |  Methods defined here:
     |
     |  myfunc(self, x, y)
     |      A sample function
