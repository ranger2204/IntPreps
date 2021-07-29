# https://leetcode.com/problems/integer-to-roman/
class Solution:
    def intToRoman(self, num: int) -> str:
        mappings = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'C',
            100:'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
            
        }

        mi = 0
        roman = ''
        while num > 0:
            
            while mi < len(mappings):
                m = list(mappings.keys())[mi]
                if m <= num:
                    num -= m
                    roman += str(mappings[m])
                    break
                mi += 1
        return roman


tests = [
    1,
    3,
    4,
    900,
    1994
]

for t in tests:
    print(Solution().intToRoman(t))    
