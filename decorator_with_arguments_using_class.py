# -*- coding: utf-8 -*-
# @Author: Pan Chao
# @Date:   2017-08-31 11:46:43
# @Last Modified by:   Pan Chao
# @Last Modified time: 2017-08-31 11:58:58

'''
Demonstrate how to use a parametrized decorator by implementing it as a class.
'''

class decorator_with_arguments(object):
    def __init__(self, arg1, arg2, arg3):
        """If there are decorator arguments, the function to be decorated is
        NOT passed to the constructor! """
        print("Inside __init__()")
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        """If there are decorator arguments, __call__() is only called once,
        as part of the decoration process! You can only give it a single argument,
        which is the function object."""
        print("Inside __call__()")
        def wrapped_f(*args, **kwargs):
            print("Inside wrapped_f()")
            print("Decorator arguments:", self.arg1, self.arg2, self.arg3)
            f(*args, **kwargs)
            print("After f(*args, **kwargs)")
        return wrapped_f


if __name__=='__main__':

    @decorator_with_arguments('hello', 'world', 42)
    def sayHello(a1, a2, a3, a4):
        print('sayHello() arguments:', a1, a2, a3, a4)

    print("After decoration")

    print("Preparing to call sayHello()")
    sayHello('say', 'hello', 'argument', 'list')
    print("after first sayHello() call")
    sayHello('a', 'different', 'set of', 'arguments')
    print("after second sayHello() call")



