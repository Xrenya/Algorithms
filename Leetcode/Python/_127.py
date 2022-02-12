import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS in graph
        # vertices are words, and two words are connected if they differ by one letter
        # How to build the graph efficiently?
        # Alternatively, the number of possible mutations from a given word is bounded by 26 * L (L length of word < 10)
        # So we can dynamically traverse the graph without creating one with use of hashset
        
        dictionary = set(wordList)
        n = len(beginWord)
        
        queue = [beginWord]
        num_words = 1
        seen = set()
        seen.add(beginWord)
        while queue:
            new_queue = []
            num_words += 1
            for word in queue:
                for i in range(n):
                    for c in string.ascii_lowercase:
                        if c != word[i]:
                            new_word = word[:i] + c + word[i+1:]
                            if new_word in dictionary:
                                if new_word == endWord:
                                    return num_words
                                if new_word not in seen:
                                    seen.add(new_word)
                                    new_queue.append(new_word)
            queue = new_queue
        return 0
    
    # Time: O(NL^2) N: # of words in dictionary and L: length of the word
    # Space: O(NL)
