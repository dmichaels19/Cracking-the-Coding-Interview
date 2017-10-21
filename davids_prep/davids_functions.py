def new_range_iter(first, second=None, increment=1):
    if second == None:
        start = 0
        end = first
    else:
        start = first
        end = second

    curr = start
    while curr < end:
        print(increment)
        yield curr
        curr += increment

def new_range_list(first, second=None, increment=1):
    return [i for i in new_range_iter(first,second,increment)]

print(new_range_list(10))

