class Solution:
    def longestPalindrome(self, s: str) -> str:
        # two cases
        # even or odd palindrome length
        # if we use recursion we can just check if the two incremental chars are valid
        # we have the two base cases of one or two chars
        # if we use sliding window from the ends we can also isolate it
        center = 0

        max_len = 1
        max_str = s[0]

        while center < len(s):
            print(center)
            left = center
            right = center
            # first try odd
            while left-1 >= 0 and right+1 < len(s):
                left -= 1
                right += 1
                # print(s[left: right + 1], right - left + 1)
                if s[left] == s[right]:
                    # valid still
                    if right - left + 1 > max_len:
                        max_len = right - left + 1
                        max_str = s[left: right + 1]
                else:
                    break

            # then try even
            if center + 1 < len(s) and s[center] == s[center + 1]:
                left = center
                right = center + 1
                if right - left + 1 > max_len:
                    # print(s[left: right+1], right - left + 1)
                    # print("here")
                    max_len = right - left + 1
                    max_str = s[left: right + 1]
                while left-1 >= 0 and right+1 < len(s):
                    left -= 1
                    right += 1
                    # print(s[left: right], right - left)
                    if s[left] == s[right]:
                        # valid still
                        if right - left + 1 > max_len:
                            max_len = right - left + 1
                            max_str = s[left: right + 1]
                    else:
                        break
            center += 1
        return max_str

       