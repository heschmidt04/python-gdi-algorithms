# Write a function called letter_count
# take in a single argument, a string of arbitrary length
# return a fixed-length array of length 26,
# where the 0 position represents the count of the letter "a"
# from the string,
# and the 1 position represents the count of b, and so on.
# Count each letter regardless of case, so the string "aaAA" should have a "4" in the 0th position

test_result = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]
print(len(test_result))


# input : "AAaa"
# [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# input : "ABCabc"
# [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# write two more test strings to test your code will work
# make sure to test edge cases- punctuation, numbers, and other characters besides letters
def letter_count(input_string):
    result = [0] * 26
    # loop over each letter
    for letter in input_string:
        letter_position = (ord(letter) - 65) % 32
        # figure out which letter this is and where it goes
        # do it with numbers
        # do it with string transformations

        # increment that count for that letter
        current_letter_count = result[letter_position]
        result[letter_position] = current_letter_count + 1

    # format the counts into an array
    # return the array
    return result


print(letter_count("ABabcDefgh"))


def letter_count_hash_map(input_string):
    result = [0] * 26
    # use this map pattern for next problem
    result_map = {}
    # loop over each letter
    for letter in input_string:
        # figure out which letter this is and where it goes
        # do it with numbers
        # letter_position = (ord(letter) - 65) % 32
        # do it with string transformations
        normalized_letter = letter.lower()

        # increment that count for that letter
        # current_letter_count = result[letter_position]
        # result[letter_position] = current_letter_count + 1
        current_letter_count = result_map.get(normalized_letter, 0)
        # result_map.get will not fail if element is not there -- will pass 0 as a default
        # if you don't know the number of buckets in advance a hash map is good for that
        result_map[normalized_letter] = current_letter_count + 1

    # format the counts into an array
    for letter_address in range(97, 123):
        # print(chr(letter_address))
        result[letter_address - 97] = result_map.get(chr(letter_address), 0)
    # return the array
    return result


print(letter_count_hash_map("ABabcdDefgh"))
