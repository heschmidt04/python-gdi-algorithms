from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Pass in a number to generate the possible list of
        combinations of parenthesis
        See https://www.youtube.com/watch?v=s9fokUqJ76A

        Better explanation -- principals of recursion aka backtracking
        https://www.youtube.com/watch?v=sz1qaKt0KGQ

        :param n:
        :return:
        """
        # Assumptions:
        # only add open parens if open < n
        # only add a closing parens if closed < open
        # valid IF open == closed == n

        # stack is the working scratch space
        stack = []
        # result is the final list of all possible permutations
        result = []

        def backtrack(openN, closedN):
            # If we have them all equal then append the patern to the results list
            if openN == closedN == n:
                result.append("".join(stack))
                return
            # When openN is less than total N of parens, keep going through to get even paren groups
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
                print(stack)
            # When closedN is less than total N of parens,
            # keep going through to get even paren groups
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
                print(stack)

        # self is the number and N is the number to be compared to a starter position
        # of 0,0 for backtrack
        backtrack(0, 0)
        return result


print(Solution.generateParenthesis(3, 3))


print(Solution.generateParenthesis(5, 5))
