def make_spiral(spiral_size):
    """
    This function creates a spiral to walk
    :param spiral_size:
    :return: array
    """
    spiral = []  # start out empty
    for x in range(spiral_size):  # spiral becomes the spiral_size in number range
        spiral.append(
            [x for x in range(spiral_size)]
        )  # list comprehension - for x in range(): append(x)
        # keep track of direction we are heading

    # spiral =
    # [[0, 1, 2, 3, 4],
    #  [0, 1, 2, 3, 4],
    #  [0, 1, 2, 3, 4],
    #  [0, 1, 2, 3, 4],
    #  [0, 1, 2, 3, 4]]

    # Starting values
    direction = "right"
    row = 0
    col = 0
    num = 1

    # keep track of the boundaries
    # spiral = [0,1,2,3,4] # check the python tutor screen shot for the value

    top_boundary = (
        1  # start the top bound at 1 , not 0 because we start at row 0 and travel right
    )
    bottom_boundary = spiral_size - 1  # which is 4

    left_bound = 0
    right_bound = spiral_size - 1  # which is 4

    limit = spiral_size * spiral_size

    # Going to while loop here
    # while left_bound < right_bound - changed to num < than limit
    while num <= limit:
        print(
            row,
            col,
            num,
            direction,
            " boundaries:",
            left_bound,
            right_bound,
            top_boundary,
            bottom_boundary,
        )

        spiral[row][col] = num  # This I get a type int unsubscriptable error

        # turn right, col++
        if direction == "right":
            if col == right_bound:
                right_bound -= 1
                direction = "down"
            else:
                col += 1
                num += 1

        # turn left, col--
        if direction == "left":
            if col == left_bound:
                left_bound += 1
                direction = "up"
            else:
                col -= 1
                num += 1

        # down, row++
        if direction == "down":
            if row == bottom_boundary:
                bottom_boundary -= 1
                direction = "left"
            else:
                row += 1
                num += 1

        # up, row--
        if direction == "up":
            if row == top_boundary:
                top_boundary += 1
                direction = "right"
            else:
                row -= 1
                num += 1

    return spiral


def print_result(result):
    for row in result:
        print(row)


print_result(make_spiral(5))
