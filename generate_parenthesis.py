def BracketCombinations(self, n):
    """
    This function BracketCombinations wraps around the function generate_parens (decorator) to
    create possible permutations combinations of left and right parenthesis
    based on the number passed into the BracketCominations Python class

    :param self:
    :param n: int
    :return: int
    """
    if n == 0:
        return 1

    def generate_parens(p, left, right, parens=[]):
        if left:
            generate_parens(p + "(", left - 1, right)
        if right > left:
            generate_parens(p + ")", left, right - 1)
        if not right:
            parens += (p,)
        return len(parens)

    return generate_parens("", n, n)


print(BracketCombinations(3, 3))
