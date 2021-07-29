import math

class Solution:
    turns = float('inf')
    PATH = []

    def find_nearest(self, pos, bypass):
        ds = float('inf')
        n = -1
        for each in bypass:
            d = each - pos
            if d > 0:
                if d < ds:
                    ds = d
                    n = each
        return n

    def find_min_turns(self, snakes, ladders, cur_pos, turns=0, marked={}):
        
        if turns >= 100:
            return 100

        if cur_pos == 100:
            if turns < Solution.turns:
                Solution.turns = turns
                Solution.PATH=marked.keys()
            return turns

        #find nearest snake
        ns = self.find_nearest(cur_pos, snakes)
        ds = ns - cur_pos
        ds = math.ceil(ds/6)

        #find nearest ladder
        nl = self.find_nearest(cur_pos, ladders)
        dl = nl - cur_pos
        dl = math.ceil(dl/6)

        if ns in marked or nl in marked:
            return 100

        
        return turns + min(
            self.find_min_turns(snakes, ladders, ladders.get(nl, -1), dl, marked | {nl : 0}), 
            self.find_min_turns(snakes, ladders, snakes.get(ns, -1), ds, marked | {ns : 0})
        )


test = {
    'snakes': {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78},
    'ladders': {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
}

print(Solution().find_min_turns(test['snakes'], test['ladders'], 0))
print(Solution.PATH)