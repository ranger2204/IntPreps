class Solution:
    def generate_valid_ips(self, start):
        valid_ips = []

        def validate_ip(s):
            if len(s) == 0 or len(s) > 3:
                return False
            if s[0] == '0' and len(s) > 1:
                return False
            if int(s) > 255:
                return False
            # if len(s) <= 3 and len(s) > 0:
            #     if (s[0] != '0' and len(s) > 1) or (s[0] == '0' and len(s) == 1):
            #         if int(s) <= 255:
            #             return True
            return True

        def recur(start, cur_index, tokens):
            nonlocal valid_ips
            if cur_index >= len(start):
                if len(tokens) == 4:
                    valid_ips.append(tokens)
                return
            else:
                s = cur_index
                for i in range(s+1, s+4):
                    t = start[s: i]
                    if validate_ip(t):
                        recur(start, i, tokens+[t])
        
        recur(start, 0, [])
        return valid_ips

tests = [
    "2542540123"
]

for t in tests:
    print(Solution().generate_valid_ips(t))