from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queue for BFS
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0
    
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
