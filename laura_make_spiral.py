# https://replit.com/@LauraSteiner1/Spiral2#main.py

## Write a function called make_spiral
## You are given one argument, called size, an integer value
## return a 2D array that outputs a spiral like so:

## input: 2
## ouput:
spiral_1 = [[1, 2], [4, 3]]

## input: 4
## ouput:
spiral_2 = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
## (note from Liz) I put spaces to make the spiral easier to see

## input: 5
## output:
spiral_3 = [
    [1, 2, 3, 4, 5],
    [16, 17, 18, 19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9],
]


# Laura notes
# algo from:
# https://www.educative.io/answers/spiral-matrix-algorithm
# 4 variables which store the outer edge for each side
# for a direction, process the full row or column of that direction
#   then adjust the edge accordingly


def make_spiral(size):
    arr = [[0 for i in range(size)] for j in range(size)]

    limit = (size * size) + 1

    num = 1
    dir = "right"
    top = 0
    bottom = size - 1
    left = 0
    right = size - 1

    while num < limit:
        if dir == "right":
            # populate this row with the proper numbers
            for i in range(left, right + 1):
                arr[top][i] = num
                num += 1
            # when finished, adjust the top edge and change direction
            top += 1
            dir = "down"
        elif dir == "down":
            for i in range(top, bottom + 1):
                arr[i][right] = num
                num += 1
            right -= 1
            dir = "left"
        elif dir == "left":
            for i in range(right, left - 1, -1):
                arr[bottom][i] = num
                num += 1
            bottom -= 1
            dir = "up"
        elif dir == "up":
            for i in range(bottom, top - 1, -1):
                arr[i][left] = num
                num += 1
            left += 1
            dir = "right"

    return arr


def print_result(result):
    for row in result:
        print(row)


print_result(make_spiral(5))
