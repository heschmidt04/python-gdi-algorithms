# ##########################################
# The algorithm to find the shape of a wave
# Homework
# Which Light?
##########################################

# You are reading a digital signal coming from a light sensor
# connected to a pin on a microcontroller.
# Your job is to figure out which light has been turned on based on it's behavior.

# You are given an unsorted list of integers
# from 0-255 representing the light level during a period of time,
# where each element is the reading for 1 millisecond of time.

# There is a fair amount of random light coming in,
# and a distinct period of time where a light is turned on.
# If a light is turned on, it will be on for a period of time longer than a few milliseconds
# - but you're not sure how long.

# Each light has a distinct pattern of lighting up:

# Halogen lights brighten slowly after an initial jump in luminosity, and dim almost instantly,
# and produce more variation in light emitted

# Florecent lights brighten faster than halogen lights,
# produce a steadier light than halogen, and dim more slowly.

# Incandecent lights brighten nearly immediately,
# and dim nearly immediately, and produce a consistent amount of light

# LED lights brighten immediately,
# dim immediately, and produce a brighter amount of consistent light than incandecent lights


# You are also not sure how bright it is in the room to begin with,
# so you cannot assume there is no light in the room to start.
# Only that an overhead light is on or off.

# Write a function that returns
#   which kind of light bulb has turned on,
#   as a string (one of "halogen", "florecent", "incandecent", "LED")

# Examples
example_one = [
    4,
    4,
    5,
    5,
    4,
    3,
    3,
    4,
    5,
    77,
    77,
    77,
    78,
    79,
    80,
    81,
    88,
    90,
    95,
    100,
    100,
    110,
    115,
    135,
    145,
    158,
    158,
    190,
    200,
    200,
    200,
    200,
    200,
    150,
    100,
    60,
    7,
    8,
    8,
    8,
]  # halogen
# halogen

example_two = [
    4,
    5,
    8,
    9,
    11,
    2,
    3,
    4,
    5,
    6,
    5,
    4,
    5,
    4,
    100,
    110,
    115,
    135,
    145,
    158,
    158,
    190,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    190,
    100,
    90,
    87,
    80,
    30,
    25,
    26,
    27,
    28,
    29,
    30,
    30,
    30,
    30,
    30,
    30,
    30,
]  # florecent
# flourescent

example_three = [
    4,
    4,
    5,
    5,
    4,
    3,
    3,
    4,
    4,
    4,
    5,
    5,
    4,
    3,
    3,
    4,
    5,
    100,
    150,
    200,
    200,
    200,
    201,
    201,
    200,
    201,
    200,
    199,
    200,
    200,
    199,
    201,
    150,
    4,
    4,
    5,
    5,
    4,
    3,
    3,
    4,
    9,
    4,
    4,
    5,
    5,
    4,
    3,
    3,
    4,
    5,
]  # incandecent
# incandescent

example_four = [
    4,
    4,
    5,
    5,
    4,
    3,
    3,
    4,
    4,
    4,
    5,
    5,
    4,
    3,
    3,
    4,
    5,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    4,
    4,
    5,
    5,
    4,
    3,
    3,
    4,
    9,
    4,
    4,
    5,
    5,
    4,
    3,
    3,
    4,
    5,
]  # LED


# LED

# The rise is the attack (for lack of a better term)
# The length of the start of when it starts to rise, to when it reaches maximum brightness
# amplitutude - the height of the wave
# sustain -- the consistency of the max


def which_light(readings):
    """
    Identify which type of light has been turned on
    Options: Halogen, Flourescent, Incadescent, LED

    :param readings:
    :return: string
    """
    attack_begin = 0
    # loop over the entire list
    for index in range(len(readings)):
        attack_end = index
        reading = readings[index]
        # take note when the first jump in light value appears
        if reading - readings[index - 1] > 60 and attack_begin == 0:
            attack_begin = index
            # keep track of how long it takes to get to 200 (length of attack)
        if reading == 200 and attack_end == 0:
            attack_end = index

    attack_length = abs(attack_begin - attack_end)
    if attack_length > 10:
        return "halogen"
    if attack_length > 5 and attack_length < 10:
        return "flourescent"
    if attack_length == 0:
        return "LED"


# check to see if there is "wobble" in the plateau (sustain)
# check the length of the "decay"
# (how long does it take to go from 200 to at least 30 brightness)
# pass


print(which_light(example_one))
print(which_light(example_two))
print(which_light(example_three))
print(which_light(example_four))
