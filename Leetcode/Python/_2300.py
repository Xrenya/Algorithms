class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        output = []

        m = len(potions)
        maxPotion = potions[m - 1]
        
        for spell in spells:
            
            min_portion = (success + spell - 1) // spell
            
            if min_portion > maxPotion:
                output.append(0)
                continue
            
            index = bisect.bisect_left(potions, min_portion)
            output.append(m - index)
            
            
        return output
