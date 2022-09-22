# python doesn't support trail recursion
# but it's simple example of this algorithm in python

def recursion_sum(x):
    if x == 0:
        return 0

    return x + recursion_sum(x - 1)


def tail_recursion_sum(x, last):
    if x == 0:
        return last

    return tail_recursion_sum(x - 1, last + x)


print(recursion_sum(10))
print(tail_recursion_sum(10, 0))
