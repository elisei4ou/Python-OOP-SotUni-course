def type_check(_type):

    def decorator(function):

        def wrapper(*args, **kwargs):
            if not isinstance(*args, _type):
                return "Bad Type"
            return function(*args)

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))

