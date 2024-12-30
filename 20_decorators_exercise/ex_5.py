def cache(func):

    def wrapper(num):
        result = func(num)
        if num not in wrapper.log:
            wrapper.log[num] = result

        return func(num)

    wrapper.log = {}

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(4)
print(fibonacci.log)



