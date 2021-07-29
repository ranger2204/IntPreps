class ValidateNumber:
    def validate(self, num_str: str) -> bool:
        dec_count = 1
        exp_count = 1
        for i,c in enumerate(num_str):
            if c.isdigit():
                continue
            elif c in ['-', '+']:
                if i != 0:
                    return False
            elif c == '.':
                if dec_count and i != 0 and exp_count > 0:
                    dec_count -= 1
                else:
                    return False
            elif c.lower() == 'e':
                if exp_count and i != 0:
                    exp_count -= 1
                else:
                    return False
            else:
                return False
        return True



tests = [
    '10',
    '-10',
    '-10.01',
    '1e10',
    '1.02e25',
    '1e0.25',
    '1.2.5urn'
]


for t in tests:
    print("{} : {}".format(t, ValidateNumber().validate(t)))
            
                
            