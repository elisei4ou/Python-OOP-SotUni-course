from time import time

def exec_time(func):

    def wrapper(*args, **kwargs):
        time_start = time
        func(*args, *kwargs)
        time_end = time
        return time_end - time_start
    return wrapper


@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1
print(loop())
