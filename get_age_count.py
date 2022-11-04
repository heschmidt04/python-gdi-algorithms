import requests

# Original imports (not needed)
# import numpy as np
# import pandas as pd

# Original values (standardized below)
# r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
# print(len(r.json()['data']))


url = "https://coderbyte.com/api/challenges/json/age-counting"
r = url
# print(r)
# print(url)
# resp = requests.get(url)
# print(resp.status_code)


def get_age_count(age_num):
    """
      Write a HTTPS get request on
      the API route https://coderbyte.com/api/challenges/json/age-counting output:
        format
          key = data key
          value: key = STRING
                 age = INTEGER

    :param: age_num: int
    :return: count of number of people with that age or greater as an integer

    >>> get_age_count(50)
    128
    >>> get_age_count(25)
    208
    >>> get_age_count(100)

    """
    url = "https://coderbyte.com/api/challenges/json/age-counting"
    resp = requests.get(url)
    # print(len(resp.json()['data']))
    requests_results_json = resp.json()["data"].split(",")
    # Set an empty counter to count the number of people found that match age
    counter = 0
    for item in requests_results_json:
        # The first split was to get the keys and values split out by comma
        # This split is to get both key (the persons key) and age (age of the person)
        #      seperated by = sign
        split_data = item.split("=")
        if split_data[0].strip() == "age" and int(split_data[1]) >= age_num:
            counter += 1
    return counter


print(get_age_count(50))
# print(get_age_count(25))
# print(get_age_count(100))

if __name__ == "__main__":
    #  import doctest
    get_age_count(50)

# The doctest definately wants cleaner code because of the failure with doctest
# Will have to test this out further to understand it better
#
# doctest.run_docstring_examples(
#    get_age_count("str")
#    , globals()
#    , verbose = True
#    , name = "get_age_count"
#  )
