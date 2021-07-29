class Solution:
    def addOperators(self, num: str, target: int):
        operators = ['-', '+', '*']
        precd = {
            '-': 0,
            '+': 0,
            '*': 1
        }
        
        def infix_to_postfix(exp):
            s = []
            r = ""
            i = 0
            while i < len(exp):
                c = exp[i]

                if c not in operators:
                    while i < len(exp) and exp[i] not in operators:
                        r += exp[i]
                        i += 1
                    r += ' '
                    continue
                else:
                    if len(s) == 0 or precd[s[-1]] < precd[c]:
                        s.append(c)
                    else:
                        while len(s)>0 and precd[c] < precd[s[-1]]:
                            r += s.pop(-1)
                        s.append(c)
                i += 1
            while len(s) > 0:
                r += s.pop(-1)
            return r
        
        def evaluate_postfix(exp):
            s = []
            i = 0
            while i < len(exp):
                c = exp[i]
                if c in operators:
                    y = int(s.pop(-1))
                    x = int(s.pop(-1))
                    if c == '*':
                        e = x*y
                    if c == '+':
                        e = x + y
                    if c == '-':
                        e = x - y
                    s.append(e)
                else:
                    val = ""
                    while exp[i] != ' ':
                        val += exp[i]
                        i+=1
                    s.append(val)
                i += 1
            return s[-1]
        
        def evaluate_exp(expr):
            postfix = infix_to_postfix(expr)
            # print(expr, postfix)
            return evaluate_postfix(postfix)
            
        
        result = []
        
        def recur(str_digits, cur_exp, index, target):
            nonlocal result
            if index >= len(str_digits):
                value = evaluate_exp(cur_exp)
                if value == target:
                    result.append(cur_exp)
            else:
                for o in operators:
                    recur(str_digits, cur_exp+o+str_digits[index], index+1, target)
                recur(str_digits, cur_exp+str_digits[index], index+1, target)
                
        recur(num, num[0:1], 1, target)
        return result


tests = [
    {
        'num': '123',
        'target': 6
    }
]

for t in tests:
    Solution().addOperators(**t)