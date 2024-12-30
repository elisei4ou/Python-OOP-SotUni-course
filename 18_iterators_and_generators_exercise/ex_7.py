def read_next(*args):
    for every_arg in args:
        yield from every_arg


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)

