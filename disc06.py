# def gen_fib():
#     n, add = 0, 1
#     while True:
#         yield n
#         n, add = n + add, n

# print((lambda t: [next(t) for _ in range(10)])(gen_fib()))

# iter = filter(lambda n: n > 2024, gen_fib())
# print(next(iter))

# def sub_generator():
#     yield 1
#     yield 2
#     return "done"  # 这个返回值会被 yield from 捕获

# def main_generator():
#     result = yield from sub_generator()
#     print(f"子生成器返回: {result}")  # 子生成器返回: done
#     yield result

# g = main_generator()
# for item in g:
#     print(item)  # 打印 1, 2, done

def differences(t):
    """Yield the differences between adjacent values from iterator t.

    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    "*** YOUR CODE HERE ***"
    prev = next(t)
    for curr in t:
        yield curr - prev
        prev = curr

def partition_gen(n, m):
    """Yield the partitions of n using parts up to size m.

    >>> for partition in sorted(partition_gen(6, 4)):
    ...     print(partition)
    1 + 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 3
    1 + 1 + 2 + 2
    1 + 1 + 4
    1 + 2 + 3
    2 + 2 + 2
    2 + 4
    3 + 3
    """
    assert n > 0 and m > 0
    if n == m:
        yield str(m)
    if n - m > 0:
        "*** YOUR CODE HERE ***"
        for p in partition_gen(n-m, m):
            yield p + ' + ' + str(m)
    if m > 1:
        "*** YOUR CODE HERE ***"
        # yield from partition_gen(n, m-1)
        for p in partition_gen(n, m-1):
            yield p 