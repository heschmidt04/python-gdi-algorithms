def keith_make_spiral(spiral_size):
    spiral = []
    for x in range(spiral_size):
        spiral.append([0] * spiral_size)

    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # right  # down  # left  # up
    direction = 0
    row = 0
    col = 0
    num = 1
    limit = spiral_size * spiral_size
    while num <= limit:
        spiral[row][col] = num

        next_row = row + directions[direction][0]
        next_col = col + directions[direction][1]
        # De Morgans first law -- instead of the OR logic
        # https://bit.ly/3fmOWhe
        if not (
            (
                (
                    (not (next_row < 0) and not (next_col < 0))
                    and not (next_row == spiral_size)
                )
                and not (next_col == spiral_size)
            )
            and not (spiral[next_row][next_col] != 0)
        ):  # time to change direction
            direction = mod(direction + 1, 4)
        else:  # go forward
            row = next_row
            col = next_col
            num += 1
    return spiral
