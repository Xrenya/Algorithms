class Solution:
    def maxNumberOfFamilies(
        self, n: int, reservedSeats: List[List[int]]
    ) -> int:
        left, middle, right = 0b11110000, 0b11000011, 0b00001111
        occupied = collections.defaultdict(int)
        for seat in reservedSeats:
            if 2 <= seat[1] <= 9:
                occupied[seat[0]] |= 1 << (seat[1] - 2)

        ans = (n - len(occupied)) * 2
        for row, bitmask in occupied.items():
            if (
                (bitmask | left) == left
                or (bitmask | middle) == middle
                or (bitmask | right) == right
            ):
                ans += 1
        return ans
      
    def maxNumberOfFamiliesV2(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved_row = defaultdict(set)
        for (row, col) in reservedSeats:
            reserved_row[row - 1].add(col)
        empty_rows = n - len(reserved_row)
        max_seats = empty_rows * 2
        for row in reserved_row.keys():
            if not reserved_row[row]:
                max_seats += 2
                continue
            
            left_free = all(c not in reserved_row[row] for c in [2, 3, 4, 5])
            right_free = all(c not in reserved_row[row] for c in [6, 7, 8, 9])
            middle_free = all(c not in reserved_row[row] for c in [4, 5, 6, 7])
            if left_free and right_free:
                max_seats += 2
            elif left_free or right_free or middle_free:
                max_seats += 1
        return max_seats
