class NextPerm:
    #find the odd
    #swap the odd one with the nearest
    def get_next(self, start: str):
        rev_str = start[::-1]
        #assuming numbers
        pivot = -1
        for i, v in enumerate(rev_str):
            if i == 0:
                continue
            else:
                if int(v) < int(rev_str[i-1]):
                    pivot = i
                    break
        
        if pivot == -1:
            return "pivot -1"
        else:
            act_pivot = len(start) - i - 1
            min_pivot = -1
            min_dff = float('inf')
            for i in range(act_pivot+1, len(start)):
                d = int(start[i]) - int(start[act_pivot])
                if d > 0 and d < min_dff:
                    min_dff = d
                    min_pivot = i
            
            if min_pivot != -1:
                str_list = list(start)
                str_list[min_pivot], str_list[act_pivot] = str_list[act_pivot], str_list[min_pivot]
                return ''.join(str_list)
            else:
                return 'min_pivot -1'

tests = [
    "123",
    "312",
    "321",
    "000",
    "48900"
]

for t in tests:
    print(NextPerm().get_next(t))