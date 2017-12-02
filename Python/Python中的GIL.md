Title: Python中的GIL
Date: 2017-08-11 16:42
Modified: 2017-08-15 09:26
Tags: python, gil

GIL，全称是Global Interpreter Lock，全局解释器锁。GIL是CPython的一个设计，而不是python语言的特性。官方对GIL解释如下

> In CPython, the global interpreter lock, or GIL, is a mutex that prevents multiple native threads from executing Python bytecodes at once. This lock is necessary mainly because CPython’s memory management is not thread-safe. (However, since the GIL exists, other features have grown to depend on the guarantees that it enforces.)
>
> 在CPython中，GIL是用来防止多个线程同时执行python的字节码的，GIL存在的主要原因是CPython的内存管理器并非线程安全的。（然而，有了GIL后，很多其他特性的实现都依赖于GIL）

在多线程编程中，后台确实有多个线程在同时运行，不过GIL的存在使得多个线程中只有一个线程在执行Python代码，其他线程需要等待GIL锁的释放才有机会执行。

GIL的好处在于，由于这把大锁的存在，python内的对象默认都是线程安全的，不必额外的再去手动加锁。在开发过程中省了很多事。

GIL的坏处在于，由于GIL的存在，是的多线程中实际上只有一个线程在执行python字节码，当一个线程执行的时候，其他的线程都在等待GIL的释放，并没有真正执行。再加上线程上下文切换花费的资源，实际上并不一定比单线程效率高。

释放GIL的条件是遇到IO操作或者字节码指令执行了一定的条数，所以对于IO密集的并发操作，Python的多线程还是有用的。