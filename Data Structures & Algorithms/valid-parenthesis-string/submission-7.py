class Solution:
    def checkValidString(self, s: str) -> bool:
        # we can do the following 
        # we advance from the sides and continue in
        # if we see a mismatch we know False
        # if we see a * we have two cases and can recurse both options if there is ambiguity
        # we SHOULD be able to just infer our only option
        # unless we can have nested parenthesis? we can

        # since we can have complex nesting we need to go in chunks
        # we will remove valid things until we have '' OR we hit an invalid sequence


        low = high = 0
        for char in s:
            if char == '*':
                low -= 1
                high += 1
            else:
                if char == '(':
                    high += 1
                    low += 1
                if char == ')':
                    high -= 1
                    low -= 1
            if low < 0:
                low = 0
            if high < 0:
                return False
        return 0 == low
