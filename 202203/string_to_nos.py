class Solution():
    def find_nos(self, inp):
        nums = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            0: "zero"
        }

        inp_list = list(inp)
        result = []
        while len(inp_list) > 0:
            for k in nums:
                new_list = inp_list[:]
                for c in nums[k]:
                    if c in new_list:
                        new_list.remove(c)
                    else:
                        break
                if len(inp_list) - len(new_list) == len(nums[k]):
                    result.append(k)
                    inp_list = new_list
        print(result)


tests = [
    'niesevehrtfeev'
]

for t in tests:
    Solution().find_nos(t)