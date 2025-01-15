class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        output = num1

        target_set_bits_count = bin(num2).count("1")
        set_bits_count = bin(output).count("1")

        current_bit = 0

        while set_bits_count < target_set_bits_count:
            if not self._is_set(output, current_bit):
                output = self._set_bit(output, current_bit)
                set_bits_count += 1
            current_bit += 1
        
        while set_bits_count > target_set_bits_count:
            if self._is_set(output, current_bit):
                output = self._unset_bit(output, current_bit)
                set_bits_count -= 1
            current_bit += 1

        return output

    def _is_set(self, x: int, bit: int) -> bool:
        return (x & (1 << bit)) != 0

    def _set_bit(self, x: int, bit: int):
        return x | (1 << bit)

    def _unset_bit(self, x: int, bit: int):
        return x & ~(1 << bit)
