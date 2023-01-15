def sum_two(a, b):
    return a + b


def min_(a, b):
    if a < b:
        return a
    return b


def min_multi(*args):
    if len(args) == 0:
        raise ValueError()
    if len(args) == 1:
        return args[0]
    rv = args[0]
    for elem in args[1:]:
        rv = min_(rv, elem)
    return rv


if __name__ == '__main__':
    print("hello")
    print("me")
    print("another feature")
