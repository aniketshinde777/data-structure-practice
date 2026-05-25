class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = [0] * 26

        for i in range(len(s)):
            index_of_s = ord(s[i]) - ord('a')
            index_of_t = ord(t[i]) - ord('a')

            freq[index_of_s] += 1
            freq[index_of_t] -= 1
        
        for i in range(len(freq)):
            if freq[i] != 0:
                return False
        
        return True

        