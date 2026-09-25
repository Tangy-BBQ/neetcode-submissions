class Solution:
    # the goal is to take a list of strings and then convert them to a single string
    # which can be then split back into the list

    # we are seeking to just find a method of using a delimiter
    # if we have 256 valid, we just need 1 out of scope char
    # of 257 we choose either 0 or 
    # a string will always end with Ω

    # we need to distinguish between NO strings and empty strings

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        return 'Ω'.join(strs) + 'Ω'

    def decode(self, s: str) -> List[str]:
        # print(s)
        if s == "":
            return []
        return s.split('Ω')[:-1]
