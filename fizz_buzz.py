# FizzBuzz


def fizz_buzz(N):
    """
    https://replit.com/@HeidiSchmidt/GDI-Technical-Interview-Prep-FizzBuzz-and-Count-Primes#main.py

    This function takes an integer N
    If N is evenly divisible by 3 then "Fizz"
    If N is evenly divisible by 5 then "Buzz"
    IF N is BOTH evenly divisible by 3 AND 5 then "FizzBuzz"

    :param N: int
    :return: string
    """
    # Print each number, from 0 to N, on a new line
    # Make the range plus one to handle 0 thru N (0 is the reason to add 1)
    for num in range(N + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("Fizzbuzz")
        # if the number is evenly divisible by 3, print "Fizz"
        elif num % 3 == 0:
            print("Fizz")
        # if the number is evenly divisible by 5, print "Buzz"
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


print(fizz_buzz(15))

print(fizz_buzz(10))

print(fizz_buzz(20))
