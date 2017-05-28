# Reference

1. [Python Advanced Topics - sys Module](http://www.python-course.eu/sys_module.php)

2. [Python Advanced Topics - Python and the Shell](http://www.python-course.eu/os_module_shell.php)

3. [Python Advanced Topics - Fork a Process](http://www.python-course.eu/forking.php)

    Forking is one of the most important aspects of Unix and Linux. When a process forks, it creates a copy of itself. More generally, a fork in a multithreading environment means that a thread of execution is duplicated, creating a child thread from the parent thread. they are identical but can be told apart. 
    
    The fork operation creates a separate address space for the child. The child process has an exact copy of all the memory of the parent process. The execution of the parent and child process is independent of each other. 
    
    Important `os.exec*` functions which can be used for a forked child process to execute an independent program:
     
    - `execl`
    - `execle`
    - `execlp`
    - `execlpe`
    - `execv`
    - `execve`
    - `execvp`
    - `execvpe`

4. [Python Advanced Topics - Threads in Python](http://www.python-course.eu/threads.php)

    A Thread or a Thread of Execution is defined in computer science as the smallest unit that can be scheduled in an operating system. Threads are normally created by a fork of a computer script or program in two or more parallel (which is implemented on a single processor by multitasking) tasks. Threads are usually contained in processes. More than one thread can exist within the same process. These threads share the memory and the state of the process. In other words: They share the code or instructions and the values of its variables. 
    
    There are two different kind of threads:
    
    - Kernel threads
    - User-space Threads or user threads
    
    Kernel Threads are part of the operating system, while User-space threads are not implemented in the kernel. 
    
    In a certain way, user-space threads can be seen as an extension of the function concept of a programming language. So a user-space thread is similar to a function or procedure call. But there are differences to regular functions, especially the return behaviour. 
    
    Every process has at least one thread, i.e. the process itself. A process can start multiple threads. The operating system executes these threads like parallel "processes". On a single processor machine, this parallelism is achieved by thread scheduling or timeslicing. 
    
    Advantages of Threading:
    
    - Multithreaded programs can run faster on computer systems with multiple CPUs, because theses threads can be executed truly concurrent.
    - A program can remain responsive to input. This is true both on single and on multiple CPU.
    - Threads of a process can share the memory of global variables. If a global variable is changed in one thread, this change is valid for all threads. A thread can have local variables.
    
    The handling of threads is simpler than the handling of processes for an operating system. That's why they are sometimes called light-weight process (LWP) 