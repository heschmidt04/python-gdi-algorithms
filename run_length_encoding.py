## Bonus Challenge: Run-Length Encoding
# You are given a perfectly square image as a string,
#       and the size of the image (each side is the same length)
# Each letter in the string is R, G or B

# Return
#       the size of the image, followed by an x, followed by the image compressed by "run-length encoding"

# Run-length encoding has the color, followed by the number of occurences of that color
# "RRRGGGBBB" with an image of size 3, should return "3xR3G3B3"


def compressSquareImage(image, size):
    """
    This function takes an image and returns the concatenation of
        size of image - assuming each side is equal
        x
        image run length encoding

    :param image: str
    :param size: int
    :return: string

    >>> compressSquareImage("RRRGGGBBB",size=3)
    '3xR3G3B3'
    >>> compressSquareImage("QGB",3)
    'This image has more than R, G, B - please review and fix'
    """
    # Read in the image does it have some other letter than RGB?
    for char in image:
        if char not in ["R", "G", "B"]:
            return f"This image has more than R, G, B - please review and fix"
    # Each letter in the string is R, G or B
    r_count = image.count("R")
    g_count = image.count("G")
    b_count = image.count("B")

    color_counts = f"R{r_count}G{g_count}B{b_count}"
    run_length_encoding = f"{size}x{color_counts}"
    # return the size of image + x + run length encoding
    return run_length_encoding


print(compressSquareImage("RRRGGGBBB", size=3))  # "3xR3G3B3"
print(compressSquareImage("RRRRRRGGGGBBBBBB", 4))  # "4xR6G4B6"
print(compressSquareImage("RRRBRRRRRRGGGGGGBBBBGBBBB", 5))  # "5xR3B1R6G6B4G1B4"

# import doctest
# doctest.run_docstring_examples(compressSquareImage(image, size), globals(), verbose=True, name="compressSquareImage")

if __name__ == "__main__":
    import doctest

    doctest.run_docstring_examples(
        compressSquareImage("str", int),
        globals(),
        verbose=True,
        name="compressSquareImage",
    )

    # doctest.testmod()
