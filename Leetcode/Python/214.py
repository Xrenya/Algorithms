def shortest_palindrome_kmp(s: str) -> str:
    """KMP / LPS Array Method. Time: O(n), Space: O(n)"""
    if not s:
        return ""
    
    # Create the combined string with a separator
    rev_s = s[::-1]
    combined = s + "#" + rev_s
    
    # Build KMP / LPS (Longest Prefix Suffix) table
    n = len(combined)
    lps = [0] * n
    for i in range(1, n):
        j = lps[i - 1]
        while j > 0 and combined[i] != combined[j]:
            j = lps[j - 1]
        if combined[i] == combined[j]:
            j += 1
        lps[i] = j
        
    # lps[-1] gives the length of the longest palindromic prefix
    longest_palindrome_prefix_len = lps[-1]
    suffix_to_reverse = s[longest_palindrome_prefix_len:]
    
    return suffix_to_reverse[::-1] + s


def shortest_palindrome_hash(s: str) -> str:
    """Rolling Hash Method. Time: O(n), Space: O(1) auxiliary space"""
    if not s:
        return ""
    
    base = 29
    mod = 10**9 + 7
    
    forward_hash = 0
    reverse_hash = 0
    power = 1
    longest_palindrome_prefix_len = 0
    
    # Compute running forward and backward hashes matching prefixes
    for i, char in enumerate(s):
        val = ord(char) - ord('a') + 1
        
        # Add char to the end of forward string
        forward_hash = (forward_hash * base + val) % mod
        # Add char to the front of reverse string
        reverse_hash = (reverse_hash + val * power) % mod
        
        power = (power * base) % mod
        
        # If hashes match, this prefix is a strong palindrome candidate
        if forward_hash == reverse_hash:
            longest_palindrome_prefix_len = i + 1
            
    suffix_to_reverse = s[longest_palindrome_prefix_len:]
    return suffix_to_reverse[::-1] + s
