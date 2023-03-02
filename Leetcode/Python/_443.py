class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        index = 0
        n = len(chars)
        while i < n:
            group_len = 1
            while i + group_len < n and chars[i + group_len] == chars[i]:
                group_len += 1
            chars[index] = chars[i]
            index += 1
            if group_len > 1:
                str_repr = str(group_len)
                chars[index:index + len(str_repr)] = list(str_repr)
                index += len(str_repr)
            i += group_len
        return index
      
      
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        counter = 1
        prev = chars[0]
        index = 0
        for i, char in enumerate(chars[1:] + ['0']):
            if prev == char:
                counter += 1
            else:
                if counter > 1:
                    chars[index] = prev
                    index += 1
                    for d in str(counter):
                        chars[index] = d
                        index += 1
                else:
                    chars[index] = prev
                    index += 1
                counter = 1
                prev = char
        if counter > 1:
            chars[index] = prev
            index += 1
            for d in str(counter):
                chars[index] = d
                index += 1
        return index
