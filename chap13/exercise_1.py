def fib(n):
    print("Computing fib({})".format(n))
    if n < 3:
        return 1
    else:
        print("Leaving fib({0}), returning {1}".format(n, fib(n-1) + fib(n-2)))
        return fib(n-1) + fib(n-2)
        


fib(5)
