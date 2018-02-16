### Fast Exponentiation
```
def power(a,n):
    if (n = 0):
        return 1
    x = power(a, int(n/2))
    if n % 2 == 0:
        return(x2)
    else:
        return(a × x^2)
```

### Multithreading vs. Multiprocessing in Python
```
def multithreading(func, args, 
                   workers):
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    return list(res)
def multiprocessing(func, args, 
                    workers):
    with ProcessPoolExecutor(work) as ex:
        res = ex.map(func, args)
    return list(res)
```
