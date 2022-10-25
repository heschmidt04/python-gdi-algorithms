# Replit
# https://replit.com/@HeidiSchmidt1/GDI-Technical-Interview-Prep-Letter-and-Word-Count#main.py

# Loom
# https://www.loom.com/share/0e070f6d52c54c739dd1ecbd7affb6bd?t=1

## Write a function called letter_count
## take in a single argument, a string of arbitrary length
## return a fixed-length array of length 26,
## where the 0 position represents the count of the letter "a"
## from the string,
## and the 1 position represents the count of b, and so on.
## Count each letter regardless of case, so the string "aaAA" should have a "4" in the 0th position

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


## input : "AAaa"
## [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

## input : "ABCabc"
## [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


## write two more test strings to test your code will work
## make sure to test edge cases- punctuation, numbers, and other characters besides letters
def letter_count(input_string):
    result = [0] * 26
    ## loop over each letter
    for letter in input_string:
        letter_position = (ord(letter) - 65) % 32
        ## figure out which letter this is and where it goes
        ## do it with numbers
        ## do it with string transformations

        ## increment that count for that letter
        current_letter_count = result[letter_position]
        result[letter_position] = current_letter_count + 1

    ## format the counts into an array
    ## return the array
    return result


print(letter_count("ABabcDefgh"))


def letter_count_hash_map(input_string):
    result = [0] * 26
    result_map = {}  ##  use this pattern for next problem
    ## loop over each letter
    for letter in input_string:
        ## figure out which letter this is and where it goes
        ## do it with numbers
        ## letter_position = (ord(letter) - 65) % 32
        ## do it with string transformations
        normalized_letter = letter.lower()

        ## increment that count for that letter
        ## current_letter_count = result[letter_position]
        ## result[letter_position] = current_letter_count + 1
        current_letter_count = result_map.get(normalized_letter, 0)
        ## result_map.get will not fail if element is not there -- will pass 0 as a default
        ## if you don't know the number of buckets in advance a hash map is good for that
        result_map[normalized_letter] = current_letter_count + 1

    ## format the counts into an array
    for letter_address in range(97, 123):
        ## print(chr(letter_address))
        result[letter_address - 97] = result_map.get(chr(letter_address), 0)
    ## return the array
    return result


print(letter_count_hash_map("ABabcdDefgh"))


## Homework
# Write a function called word_count
## take in a single argument, a string of arbitrary length
## output a dictionary with a count of each occurance of every word
## ensure that case is not taken into account, as in "the" and "The" should both count as "the"

## input: "dog dog cat cat"
## output: {"dog": 2, "cat": 2}

## input: "red Fish blue fish one Fish two fish"
## output: {"red": 1, "fish": 4, "blue": 1, "one": 1, "two": 1}

## input: "I remember I put on my socks, I remember I put on my shoes. I remember I put on my tie That was printed In beautiful purples and blues. I remember I put on my coat, To look perfectly grand at the dance, Yet I feel there is something I may have forgot— What is it? What is it?.." (Shel Silverstien)
## output: {'i': 10, 'remember': 4, 'put': 4, 'on': 4, 'my': 4, 'socks,': 1, 'shoes': 1, 'tie': 1, 'that': 1, 'was': 1, 'printed': 1, 'in': 1, 'beautiful': 1, 'purples': 1, 'and': 1, 'blues': 1, 'coat': 1, 'to': 1, 'look': 1, 'perfectly': 1, 'grand': 1, 'at': 1, 'the': 1, 'dance': 1, 'yet': 1, 'feel': 1, 'there': 1, 'is': 3, 'something': 1, 'may': 1, 'have': 1, 'forgot': 1, 'what': 2, 'it': 2}
def word_count(input_string):
    """
    Suggest to split the string work into two functions
    Tokenizing is the work to remove puctuation

    """
    result_map = {}
    ## create a placeholder dictionary of 26 places for letters
    word_list = input_string.lower()
    word_list = input_string.split(" ")
    size = len(input_string.split(" "))
    result = [0] * size
    ##  use this map pattern from previous letter_count function
    word_count_map = {}
    ## loop over the words in the input_string
    for word in input_string:
        normalized_word = word.lower()
        print(word)
        ## if the word does not exist - add it to the map
        current_word_count = word_count_map.get(normalized_word, 0)
        ## word_count_map.get will not fail if element is not there -- will pass 0 as a default
        ## if you don't know the number of buckets in advance a hash map is good for that
        word_count_map[normalized_word] = current_word_count + 1

    ## format the counts into an array
    for letter_address in range(97, 123):
        ## print(chr(letter_address))
        result[letter_address - 97] = result_map.get(chr(letter_address), 0)
    ## return the array
    return result
