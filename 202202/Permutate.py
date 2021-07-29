class Solution:
    def find_all_perms(self, start):
        result = []
        def recur(start: str, index: int = 0) -> list:
            nonlocal result
            if index >= len(start):
                result.append(start)
            else:
                start_list = list(start)
                for i in range(index, len(start)):
                    if index != i and start_list[index] == start_list[i]:
                        continue

                    start_list[index], start_list[i] = start_list[i], start_list[index]
                    new_start = ''.join(start_list)
                    recur(new_start, index+1)

        recur(start)
        return result

tests = [
    'AMX',
    'ABCD',
    'X',
    'AAA'
]

for t in tests:
    result = Solution().find_all_perms(t)
    print(result)