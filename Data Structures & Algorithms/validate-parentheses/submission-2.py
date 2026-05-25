class Solution:
    def isValid(self, s: str) -> bool:
        freq = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []
        for current_char in s:
            if current_char not in freq:
                stack.append(current_char)
            else:
                value = freq[current_char]
                if stack and stack.pop() == value:
                    continue
                else:
                    return False
        return True if not stack else False
