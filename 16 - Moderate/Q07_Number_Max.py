import sys

def maximum(a, b):
    index = ((a-b) >> sys.getsizeof(a-b)) + 1
    answer = a * index + b * (index ^ 1)
    return answer

if __name__ == "__main__":
    for a, b in [(x, y) for x in range(-1000, 1000) for y in range(-1000, 1000)]:
        assert maximum(a,b ) == max(a,b)