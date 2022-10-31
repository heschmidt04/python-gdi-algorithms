# This is a big thing folks get tested
# Replit is here at https://bit.ly/3WbMaMp

import pprint

pp = pprint.pprint


"""
# Write a function called analyze_logs that will accept logs as a string
You are a Site Reliability Engineer, and you have a giant pile of logs to look through.
We need to know what the most frequent error is,
and what kinds of errors there are, and under what HTTP response code they will fall
"""

raw_logs = """
[WARNING] 403 Forbidden: No token in request parameters
[ERROR] 500 Server Error: int is not subscriptable
[INFO] 200 OK: Login Successful
[INFO] 200 OK: User sent a message
[ERROR] 500 Server Error: int is not subscriptable
[WARNING] 403 Forbidden: No token in request parameters
[ERROR] 500 Server Error: int is not subscriptable
[INFO] 200 OK: Login Successful
[ERROR] 500 Server Error: int is not subscriptable
[ERROR] 500 Server Error: int is not subscriptable
[INFO] 200 OK: User sent a message
[ERROR] 500 Server Error: int is not subscriptable
[WARNING] 403 Forbidden: No token in request parameters
[INFO] 200 OK: Login Successful
[INFO] 200 OK: User sent a message
[INFO] 200 OK: Login Successful
[INFO] 200 OK: User sent a message
[INFO] 200 OK: Login Successful
[INFO] 200 OK: User sent a message
[ERROR] 500 Server Error: int is not subscriptable
[INFO] 200 OK: Login Successful
[INFO] 200 OK: User sent a message
[ERROR] 500 Server Error: int is not subscriptable
"""


def analyze_logs(logs):
    """

    You are a Site Reliability Engineer, and you have a giant pile of logs to look through.
    We need to know
            what the most frequent error is,
            and what kinds of errors there are,
            and under what HTTP response code they will fall

    analyze_logs function takes logs as a string,
     then parses through the lines to see the frequency of occurance of:
            Log_level (error, info, warning)
            HTTP status_code (200, 400) etc.
            HTTP status_message (ok, server error, forbidden)
            HTTP message body (human readable information message)

    :param logs:
    :return: dictionary with logging statistics

    Formattted output example: using pretty print to return it nicer

    output = {
    'WARNING': {
            '403': {
                    'Forbidden': {
                            'No token in request parameters': 3
                                            }
                            }
                    }
            }

    """
    # Make the output human readable - mostly
    import pprint

    pp = pprint.pprint

    # Define the output dictionary
    output = {}

    # Parse through the string and split on new lines
    for line in raw_logs.split("\n"):
        # if blank then skip it
        if not line:
            continue
        # looking for the following pieces to split out
        # log level (info, warn, error)
        # http response (200, 500, 403, etc)
        # message (everrything after the : )
        # split the line on colon
        colon_split = line.split(":")
        # colon_split is now in 2 pieces --> word_split 0 and 1
        word_split = colon_split[0].split(sep=" ", maxsplit=2)
        log_level = word_split[0].strip("[|]")
        status_code = word_split[1]
        status_message = word_split[2]
        message_count = colon_split[1].lstrip()

        # Instead of trying to slice a list
        # use the dictionary to get set dictionary keys within the main dictionary
        if log_level not in output.keys():
            # Looking for the existence of a key - set the log level dictionary
            output[log_level] = {}
        # Looking for the existence of each part of the dictionaries within the dictionary
        if status_code not in output[log_level].keys():
            output[log_level][status_code] = {}
        if status_message not in output[log_level][status_code].keys():
            output[log_level][status_code][status_message] = {}
        if message_count not in output[log_level][status_code][status_message].keys():
            # This is the COUNTER for how many times this message occurs in the log files
            output[log_level][status_code][status_message][message_count] = 0
        # Increment the counter
        output[log_level][status_code][status_message][message_count] += 1

    return pp(output)


print(analyze_logs(raw_logs))

# Return a dictionary with logging statistics,
# that is formatted like so ( don't worry about spacing or formatting, only the data matters )


output = {
    "WARNING": {"403": {"Forbidden": {"No token in request parameters": 3}}},
    "ERROR": {"500": {"Server Error": {"int is not subscriptable": 8}}},
    "INFO": {"200": {"OK": {"Login Successful": 6, "User sent a message": 6}}},
}

# When printed it will more likely look like this:
printed_output = {
    "WARNING": {"403": {"Forbidden": {"No token in request parameters": 3}}},
    "ERROR": {"500": {"Server Error": {"int is not subscriptable": 8}}},
    "INFO": {"200": {"OK": {"Login Successful": 6, "User sent a message": 6}}},
}

# output["WARNING"]["403"]["Forbidden"]["No token in request parameters"]  # 3
