
class Solution:
    def characterReplacement(self, input: str, k: int) -> int:
        freq = {}

        maxF = 0
        res = 0
        l = 0

        for r in range(len(input)):
            freq[input[r]] = freq.get(input[r], 0) + 1

            maxF = max(maxF, freq[input[r]])

            while (r-l+1) - maxF > k:
                freq[input[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res