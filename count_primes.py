def count_prime_numbers(n):
    """
    This function takes in an array of numbers to count the prime numbers in it.
    Reference: https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-68.php

    :param n:
    :return: int
    """
    counter = 0
    for num in range(n):
        if num <= 1:  # if num == 0 - skip it
            continue
        for idx in range(2, num):  # for idx position in range 2 to number n
            if (num % idx) == 0:  # this logic -- hmm
                break
        else:
            counter += 1
    return counter


print(count_prime_numbers(10))
print(count_prime_numbers(100))
