class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0
        while n > 1:
            count += n // 2
            n = n // 2 if n % 2 == 0 else n // 2 + 1
        return count


class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n != 1:
            if n % 2 == 0:
                matches += n // 2
                n /= 2
            else:
                matches += (n - 1) // 2 
                n = (n - 1) / 2 + 1
        return int(matches)
      
      
class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n != 1:
            if n % 2 == 0:
                matches += n // 2
                n //= 2
            else:
                matches += (n - 1) // 2 
                n = (n - 1) // 2 + 1
        return matches


class Solution:
    def calc(self, n, matches):
        if (n == 1):
            return 0

        if n % 2 == 0:
            matches = n // 2
            n //= 2
            return (matches + self.calc(n, matches))

        if n % 2 != 0:
            matches = (n-1) // 2
            n = (n-1) // 2 + 1
            return matches + self.calc(n, matches)
        
    def numberOfMatches(self, n: int) -> int:
        return self.calc(n, 0)
                
