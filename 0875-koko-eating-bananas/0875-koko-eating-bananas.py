class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r,l  = max(piles), 1
        res = max(piles)
        while( l<=r):
            k = (l + r)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            if hours <= h:
                res = min(k, res)
                r = k - 1
            else:
                l = k + 1
        return res
            

          

        