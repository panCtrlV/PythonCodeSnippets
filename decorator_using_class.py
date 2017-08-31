'''
Demonstrate how to use decorator by implementing it as a class.

@author: panc
@date: 2018-08-31
'''

class entry_exit(object):

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print('Entering', self.f.__name__)
        self.f()
        print('Exited', self.f.__name__)


if __name__=='__main__':

    @entry_exit
    def func1():
        print("Inside func1()")

    @entry_exit
    def func2():
        print("Inside func2()")

    func1()
    func2()
