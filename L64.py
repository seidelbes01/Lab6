#The author's names are Sydney Eidelbes and Leena Bradley

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1)+fib(n-2)

