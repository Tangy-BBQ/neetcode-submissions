class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # this seems like a backtracking problem
        # we basically choose each letter incrementally and add it to a list
        # on a new number we copy the current list, then make new combos for each

        # we need a map/list of nums to letters

        if digits == "":
            return []

        num_let = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        def rec(digits):
            # print(digits)
            if len(digits) == 1:
                return list(num_let[digits[0]])
            head = digits[0]
            tail = digits[1:]

            combos = rec(tail)
            new_combos = []

            # for each letter and each combo, we make the new one
            for letter in list(num_let[digits[0]]):
                for combo in combos:
                    new_combos.append(letter + combo)
            return new_combos
        return rec(digits)



        