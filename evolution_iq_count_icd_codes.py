icd_codes = [
    ["icd_2", "icd_3", "icd_4"],
    ["icd_1", "icd_2", "icd_3"],
    ["icd_3", "icd_5"],
]

output = {}


def count_icd_codes(icd_codes):
    """
    This function takes in a list of icd_codes
    The function returns a dictionary of code and the count of each code

    :param icd_codes:
    :return: dict

    >>> count_icd_codes([['icd_2', 'icd_3', 'icd_4']
    , ['icd_1', 'icd_2', 'icd_3']
    , ['icd_3', 'icd_5']])
    {'icd_2': 2, 'icd_3': 3, 'icd_4': 1, 'icd_1': 1, 'icd_5': 1}
    """
    for element in icd_codes:
        for code in element:
            if code not in output:
                output[code] = output.get(code)
                output[code] = 0
            output[code] += 1
    return output


print(count_icd_codes(icd_codes))

if __name__ == "__main__":
    import doctest

    doctest.run_docstring_examples(
        count_icd_codes("str"), globals(), verbose=True, name="count_icd_codes"
    )
