def even_parameters(function):

    def wrapper(*args, **kwargs):
        for el in args:
            if not isinstance(el, int):
                return "Please use only even numbers!"
            elif el % 2 != 0:
                return "Please use only even numbers!"

        return function(*args, **kwargs)

    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))



