def count_primes(n):
    """
    This function takes in an array of numbers to count the prime numbers in it.

    :param n:
    :return: int
    """
    # array to contain the primes
    prime_numbers = [2]
    # array of primes to check against
    # check each number against each of the prime_numbers array
    for i in range (2,n):
        is_prime = True
        for prime in prime_numbers:
            # if it is divisible by a prime number
            #   then it is prime and it is added to prime_number list
            if i % prime == 0:
                print(i, "isn’t a prime number.")
                is_prime = False
                # Not sure how to exit
                break
        if is_prime:
            prime_numbers.append(i)
    return len(prime_numbers)


count_primes(20)