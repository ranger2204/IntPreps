class Solution:
    @staticmethod
    def encode(strs) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + '/' + s
        return result
    
    @staticmethod
    def decode(s: str):
        i = 0
        result = []
        while i < len(s):
            l = ""
            for j in range(i, len(s)):
                if s[j] == '/':
                    i = j + 1
                    break
                l += s[j]
            
            str_len = int(l)
            word = ""
            for j in range(i, i+str_len):
                word += s[j]
            result.append(word)
            i = i + str_len
            
        return result



tests = [
    ["I", "am", "good"],
    ["lint", "code", "love", "you"]
]


for t in tests:
    encode = Solution.encode(t)
    decode = Solution.decode(encode)
    print(t, encode, decode)
        