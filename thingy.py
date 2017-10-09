import random

def thingy(arr):
    minimum = float('inf')
    m = None
    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i] and m is None:
            m = i
            if arr[i] < min:
                minimum = a[i]
    j = m - 1
    while j >= 0:
        if arr[j] > minimum:
            m -=  1
        else:
            break
        j -= 1
    return m

a = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

m = thingy(a)
for i in range(len(a)):
    a[i] *= -1
print(a)
a.reverse()
print(a)
b = a[:]
n = thingy(b)



print('(' + str(m) + ', ' + str(n) + ')')

tester = []
for i in range(20):
    tester[i] = random.randrange(20)
print(tester)