class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def feasible(eat_rate):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / eat_rate)
            
            return hours <= h
        
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2

            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left