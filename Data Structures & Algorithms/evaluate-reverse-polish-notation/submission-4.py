class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # this is basically an AST parsing question
        # the main difference is that we do not have things automatically grouped into sublists
        # we can just check if something is a number or not
        # we have the current stuff and then the new stuff
        # should be able to iterate or recurse
        
        # we have three elements
        # prev, cur, op, and next
        # prev will always be our result from the last completed operation

        # it seems like we need to parse in a different way
        # we are not grouped into triples
        # the way we can do this is by iterating until we hit our first op
        # we would then want to take the previous two numbers 
        # we compute this operation and collapse it from 3 into 1
        # the main issue will be indexing but we can do this with a while loop and a modular list

        i = 0

        while len(tokens) > 1:
            if tokens[i] in '+-*/':
                # we found an operation and need the previous 2
                v1 = tokens[i-2]
                v2 = tokens[i-1]
                
                # we need to now compute the operation
                new = 0
                if tokens[i] == '+':
                    new = int(v1) + int(v2)
                elif tokens[i] == '-':
                    new = int(v1) - int(v2)
                elif tokens[i] == '*':
                    new = int(v1) * int(v2)
                elif tokens[i] == '/':
                    new = int(int(v1) / int(v2))
                # print(v1, tokens[i], v2, '=', new)
                # we now collapse tokens
                # 3 cases
                
                if i - 3 < 0:
                    if i + 1 >= len(tokens):
                        return new
                    tokens = [str(new)] + tokens[i+1:]
                else:
                    # otherwise we have more operations
                    tokens = tokens[:i-2] + [str(new)] + tokens[i+1:]
                # print(tokens)
                # we now need to properly adjust i
                i -= 2
            i += 1
        return int(tokens[0])

        # prev = int(tokens[0])
        # cur = 0
        # for i in range(1,len(tokens)):
        #     # print(prev, tokens[i], cur)
        #     if tokens[i].isdigit():
        #         cur = tokens[i]
        #     else:
        #         if tokens[i] == '+':
        #             prev = prev + int(cur)
        #         elif tokens[i] == '-':
        #             prev = prev - int(cur)
        #         elif tokens[i] == '*':
        #             prev = prev * int(cur)
        #         elif tokens[i] == '/':
        #             prev = prev / int(cur)
        # return prev