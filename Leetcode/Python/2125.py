class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        output = 0
        prev = 0
        for row in bank:
            count = 0
            for c in row:
                if c == "1":
                    count += 1
            if count:
                output += count * prev
                prev = count
        return output
