"""
# You are an engineer at a new Natural Language Processing startup!
# Your first task is to build a natural language calculator,
# so that we can get accurate math from machines.

# Write a function called natural_language_calculator
# that will take in a single string argument,
# and output the answer as a number

# Constraints: You will only be asked to identify a single operation

# The format of the input can be counted on
#     (it will always be "operation number conjunction number")

# Input: add two and four
# Output: six

# Input: add twenty three and sixty eight
# Output: ninety one

# Input: divide one hundred by five
# Output: twenty

# Input: multiply three and five
# Output: fifteen
"""

translation_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "fourty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
    "hundred": 100,
    "thousand": 1000
}


translation_map.get("hundred",)
# 100

# Word2Number will make things easier but for now going with translation map for exercise
# Then try it with word to number afterwards
# from word2number import w2n
## Reference https://www.geeksforgeeks.org/python-convert-numeric-words-to-numbers/

## See Loom of the session for working through the javascript
## https://www.loom.com/share/0e070f6d52c54c739dd1ecbd7affb6bd?t=1

def translate_number_to_words(num):
    """
    This function takes the words for
    addition, multiplication, subtraction, and division up to hundred
    It returns the numeric equivalent of the word for the number

    :param num: int
    :return: str
    """
    hundreds = num // 100
    # floor divide tens to avoid float, then get to the ones, then times that by 10
    tens = ((num - (hundreds * 100)) // 10 ) * 10
    ones = (num % 10)

    print(hundreds, tens, ones)

    hundreds_text = translation_map.get(hundreds,"zero")
    tens_text = translation_map.get(tens)
    ones_text = translation_map.get(ones)

    print(num, hundreds_text, tens_text, ones_text)

    #if hundreds > 0:
     #   hundred_text = translation_map.get(hundreds,) + "hundred"
     #   tens_text = translation_map.get(tens,)
     #   ones_text = translation_map.get(ones,)
     #   print(num, hundreds_text, tens_text, ones_text)

    if hundreds > 0:
        return f"{hundreds_text} + {tens_text} + {ones_text}"

    if tens > 0 and hundreds == 0:
        return f"{tens_text} + {ones_text}"

    return ones_text

# checks to make sure the numbers translate
print(translate_number_to_words(100))
## 1 0 0
## 100 one zero zero
# 'one + zero + zero'

print(translate_number_to_words(1000))
## 10 0 0
## 1000 ten zero zero
# 'ten + zero + zero'

print(translate_number_to_words(10000))
## 100 0 0
## 10000 one hundred zero zero
# 'one hundred + zero + zero'

def translate_number(num_string):
    """
    Find the number based on the string

    :param num_string: string
    :return:
    """
    output_num = 0
    num_words = num_string.split(" ")

    for word in num_words:
        if word == "hundred":
            ## do some backtracking
            num = translation_map.get(last_word,0)
            output_num -= int(num)
            output_num += int(num) * 100
            continue

        num = translation_map.get(word,0)
        output_num += num
        last_word = word

    return output_num

def natural_language_calculator(user_input):
    """
    This function takes the words and does the math
    key words: add, multiply, divide
    extra words: by, and

    It relies on functions
        translate_number

    :param user_input:
    :return: string # note - not a number aka integer
    """
    ## split the user_input into words
    words = user_input.split(" ")
    ## which operation am I doing?
    first_word = words[0]
    number_string = " ".join(words[1:])
    ## what is the first number and what is the second number?
    ##word[1] and word[2]
        ## Look at the first word
        ## if it is add, do addition
        ## if it is subtract, do subtraction,
        ## if it is divide, do division
    ## depending on the operation, perform the operation
    if first_word == "add":
        numbers = user_input.split(" and ")
        first_number = translate_number(numbers[0])
        second_number = translate_number(numbers[1])
        print(numbers, first_number, second_number)
        output_num = first_number + second_number

    if first_word == "subtract":
        numbers = user_input.split(" and ")
        first_number = translate_number(numbers[0])
        second_number = translate_number(numbers[1])
        print(numbers, first_number, second_number)
        output_num = first_number - second_number

    if first_word == "divide":
        numbers = user_input.split(" and ")
        first_number = translate_number(numbers[0])
        second_number = translate_number(numbers[1])
        print(numbers, first_number, second_number)
        output_num = first_number / second_number

    if first_word == "multiply":
        numbers = user_input.split(" by ")
        first_number = translate_number(numbers[0])
        second_number = translate_number(numbers[1])
        print(numbers, first_number, second_number)
        output_num = first_number * second_number

    print(words)

    ## translate the output into natural language
    ## return the output
    translate_number_to_words(output_num)

print(natural_language_calculator("add twenty three and sixty eight"))