class Solution(object):
    def BruteLengthOfLongestSubstring(self, s):
        """
        Just sliding window without a hash map
        
        Elemetns are added to the array on each iteration
        and if an element is not in the list, but 
        if the element is already there we slice the 
        array to cut of the tail including the founded element
        
        :type s: str
        :rtype: int
        """
        window = []
        maximum = 0
        for string in s:
            if string not in window:
                window.append(string)
            else:
                # Find the index of a founded element 
                idx = window.index(string)
                # Resize the array by cutting of the tail 
                window = window[idx+1:]
                # Append the founded element 
                window.append(string)
            # Compare the current lenght of the array 
            # with the maximum
            if len(window) > maximum:
                maximum = len(window)
        return maximum

    def lengthOfLongestSubstring(self, s):
        """
        Sliding window with a hash map
        :type s: str
        :rtype: int
        """
        longest = 0
        l = 0
        lib = {}
        for r,c in enumerate(s):
            if c in lib:
                if l < lib[c] + 1:
                    l = lib[c] + 1
            lib[c] = r
            if longest < r - l + 1:
                longest = r - l + 1
        return longest
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = ""
        hashmap = {}
        n = len(s)
        lenght = 0
        for c in s:
            if c not in hashmap:
                hashmap[c] = 1
                string += c
                lenght = max(lenght, len(hashmap))
            else:
                for i in range(len(string)):
                    if c != string[i]:
                        del hashmap[string[i]]
                        continue
                    else:
                        break
                string = string[i + 1:] + c                
        return lenght
