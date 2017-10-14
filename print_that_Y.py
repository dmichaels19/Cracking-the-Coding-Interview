"""
Print a ‘Y’ shaped pattern from asterisks in N number of lines.
"""

def print_pretty(arr):
    for i in arr:
        print(i)


def print_Y(N):
    if N % 2 != 0:
        print("Noperz: Not div by 2")
        return None

    rows = 0
    for i in range(N/2, 0, -1):
        print " "*(N/2-i) + "*" + " "*(i*2 - 1) + "*" + " "*(N-i)
    for i in range(N/2):
        print " "*(N/2) + "*" + " "*(N/2)

print_Y(20)