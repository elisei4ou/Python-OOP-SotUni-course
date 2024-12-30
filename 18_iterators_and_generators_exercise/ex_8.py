from math import isqrt
from typing import List


def get_primes(numbers: List[int]):
    for n in numbers:
        if n <= 1:
            continue

        for divisor in range(2, isqrt(n) + 1):
            if n % divisor == 0:
                break

        else:
            yield n


print(list(get_primes([22])))