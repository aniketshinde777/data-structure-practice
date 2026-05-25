class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}

        start = 0
        max_length = 0
        for end in range(len(s)):
            freq[s[end]] = freq.get(s[end], 0) + 1

            while freq[s[end]] > 1:
                freq[s[start]] -= 1
                start +=1
            max_length = max(end - start + 1, max_length)

        return max_length

# s = 0
# e = 0        
# freq = 
# z x y z x y z

        

        