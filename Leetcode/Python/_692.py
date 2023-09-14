class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)

class Heap:
    def __init__(self):
        self.a = []
        self.size = 0

    def insert(self, val, char):
        self.a.append((val, char))
        self.size += 1
        j = self.size - 1
        while j > 0 and self.a[j][1] > self.a[(j - 1) // 2][1]:
            self.a[j], self.a[(j - 1) // 2] = self.a[(j - 1) // 2], self.a[j]
            j = (j - 1) // 2

    def pop(self):
        self.a[0], self.a[-1] = self.a[-1], self.a[0]
        self.size -= 1
        remove = self.a.pop()
        i = 0
        while 2 * i + 1 < self.size:
            j = 2 * i + 1
            if 2 * i + 2 < self.size and self.a[j][1] < self.a[2 * i + 2][1]:
                j = 2 * i + 2
            if self.a[i][1] > self.a[j][1]:
                break
            self.a[j], self.a[i] = self.a[i], self.a[j]
            i = j
        return remove


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        heap = Heap()
        for char, count in cnt.items():
            heap.insert(count, Pair(char, count))

        output = []
        for _ in range(k):
            output.append(heap.pop()[1].word)
        return output
