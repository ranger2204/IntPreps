class Solution:

    def get_general_abbr(word: str):
        result = []

        def recur(word, index, cur="", pos=0):
            nonlocal result
            if index >= len(word):
                result.append(cur)
                
            for i in range(0, len(word)+1):
                if i == 0:
                    recur(word, index+1, cur)

        recur(word, 0)
        return result

tests = [
    'word'
]

# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

for t in tests:
    print(Solution.get_general_abbr(t))
