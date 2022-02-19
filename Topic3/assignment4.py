from ast import Num
from sqlalchemy import false


class Number():

    def gen_primes(m, n):
        primes = []
        for num in range(m, n + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    primes.append(num)
        return primes

    def fib(n):
        a, b = 0, 1
        fib_series = []
        for _ in range(n):
            fib_series.append(a)
            a, b = b, a + b
        return tuple(fib_series)

    def reverse(num):
        num_string = str(num)
        num_string = num_string[::-1]
        return int(num_string)

    def palindrome(num):
        num_string = str(num)
        i = 0
        while i < len(num_string):
            if i == 0:
                if num_string[i] == num_string[len(num_string)-1]:
                    i += 1
                    continue
            if num_string[i] == num_string[len(num_string)-i-1]:
                i += 1
                continue
            else:
                return False
        return True

    def is_prime(num):
        if num > 1:
            for i in range(2, int(num/2)+1):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False


print(Number.is_prime(40))
