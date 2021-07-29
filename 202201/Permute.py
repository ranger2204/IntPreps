class Permute:
    def compute(self, base_str):
        all_perms = []

        def recur(base_str, cur_index=0):
            if cur_index >= len(base_str):
                print(base_str)
            else:
                for i in range(cur_index, len(base_str)):
                    list_base = list(base_str)
                    list_base[cur_index], list_base[i] = list_base[i], list_base[cur_index]
                    new_base = ''.join(list_base)
                    recur(new_base, cur_index+1)

        recur(base_str)

tests = [
    '123'
]

for t in tests:
    Permute().compute(t)