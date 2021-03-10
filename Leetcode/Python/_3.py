class Solution(object):
    def BruteLengthOfLongestSubstring(self, s):
        """
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
