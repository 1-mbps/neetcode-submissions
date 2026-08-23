from math import ceil

def num_hours(piles: List[int], k: int) -> int:
    return sum([ceil(i/k) for i in piles])

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        o = r
        while l <= r:
            m = (l+r) // 2
            hrs = num_hours(piles, m)
            if hrs > h:
                l = m+1
            elif hrs <= h:
                o = m
                r = m-1
        return o
            

        