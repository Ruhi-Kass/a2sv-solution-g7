from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # Sort in ascending order
        piles.sort()
        
        n = len(piles) // 3
        total = 0
        
        
        for i in range(n, len(piles), 2):
            total += piles[i]
        
        return total