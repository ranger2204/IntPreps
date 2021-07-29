class Solution:
    def reverse_with_delims(self, inp):
        tokens = []
        cur_token = ""
        pattern = ""
        for i in range(len(inp)):
            c = inp[i]
            if c.isalpha():
                cur_token += c
            else:
                if len(cur_token) > 0:
                    pattern += 'w'
                    tokens.append(cur_token)
                pattern += c
                
                cur_token = ""

        if len(cur_token) != 0:
            pattern += 'w'
            tokens.append(cur_token)
        tokens = tokens[::-1]
        token_index = 0
        out_str = ""
        for c in pattern:
            if c == 'w':
                out_str += tokens[token_index]
                token_index += 1
            else:
                out_str += c
        return out_str



tests = [
    "hello/world:here",
    "hello/world:here/", "hello//world:here"
]


for t in tests:
    print(Solution().reverse_with_delims(t))