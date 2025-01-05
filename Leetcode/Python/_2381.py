class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        dif = [0] * n

        for start, end, direction in shifts:
            if direction == 1:  # forward
                dif[start] += 1
                if end + 1 < n:
                    dif[end + 1] -= 1
            else:
                dif[start] -= 1
                if end + 1 < n:
                    dif[end + 1] += 1
        output = list(s)
        number_of_shift = 0

        for i in range(n):
            number_of_shift = (number_of_shift + dif[i]) % 26
            if number_of_shift < 0:
                number_of_shift += 26
            shift_char = chr(
                (ord(s[i]) - ord("a") + number_of_shift) % 26 + ord("a")
            )
            output[i] = shift_char
        return "".join(output)
