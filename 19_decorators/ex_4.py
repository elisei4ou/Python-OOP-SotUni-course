def multiply(num):

    def decorator(function):

        def wrapper(number):
            result = function(number)
            return num * result
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))


