# Write a function called excel_to_column_number
# that will take a positive integer, N.
#
# Return the equivalent column number in Excel.
# For simplicity,
# we’ll skip over the “AA” column behavior
# and simply convert to a base-26 number,
# using alpha characters as digits.

# For Example:
# A=0
# B=1
# C=2
# Z=25
# BA=26
# BB=27
# BC=28

# From GDI course
def excel_to_column_number(N):
    """
    Take a number and convert it to the Excel column position aka location

    :param N:
    :return: string
    """
    output = "" # set up a string
    while N > 0:
    # find the remainder of the number % 26 (the number of characters)
        remainder = N % 26
        letter = chr(remainder + 97) # the letter is in the alphabetical characters range
    #   put that character in the next
        output = letter + output
        N = N//26 # floor division used here to get an integer
    return output

print(excel_to_column_number(8))
print(excel_to_column_number(26))
print(excel_to_column_number(702))
print(excel_to_column_number(2400))

"""
Reference: https://stackoverflow.com/questions/48983939/convert-a-number-to-excel-s-base-26 

The problem when converting to Excel’s “base 26” is that 
for Excel, a number ZZ is actually 26 * 26**1 + 26 * 26**0 = 702 
while normal base 26 number systems would make 
a 1 * 26**2 + 1 * 26**1 + 0 * 26**0 = 702 (BBA) out of that. 
So --->  we cannot use the usual ways here to convert these numbers.
"""


def divmod_excel(n):
    a, b = divmod(n, 26)
    if b == 0:
        return a - 1, b + 26
    return a, b
# With that, we can create a to_excel function:

import string
def to_excel(num):
    chars = []
    while num > 0:
        num, d = divmod_excel(num)
        chars.append(string.ascii_uppercase[d - 1])
    return ''.join(reversed(chars))
# For the other direction, this is a bit simpler

from functools import reduce
def from_excel(chars):
    return reduce(lambda r, x: r * 26 + x + 1, map(string.ascii_uppercase.index, chars), 0)


to_excel(702)
#'ZZ'
to_excel(703)
#'AAA'
to_excel(2400)
# 'CNH'