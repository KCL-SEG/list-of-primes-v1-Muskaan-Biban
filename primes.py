"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes >= 1:
        list.append(2)
        if number_of_primes >= 2:
            list.append(3)
    number = 4
    while len(list) > number_of_primes:
        list.append(number)
        number =+ 1
    return list

primes(10)