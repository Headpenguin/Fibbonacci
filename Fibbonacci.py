def fib(n):
    a = 0
    b = 1
    c = 0
    for x in range(0, n):
        c = b
        b += a
        a = c
    print(b)
fib(100)
