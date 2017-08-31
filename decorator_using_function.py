'''
Demonstrate how to use decorator by implementing it as a function.

@author: panc
@date: 2018-08-31
'''

def entry_exit(f):
    def new_f():
        print('Entering', f.__name__)
        f()
        print('Exited', f.__name__)
    return new_f


if __name__=='__main__':

    @entry_exit
    def func1():
        print('Inside func1()')

    @entry_exit
    def func2():
        print('Inside func2()')

    func1()
    func2()
    print(func1.__name__)