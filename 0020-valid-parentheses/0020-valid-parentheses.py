class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        opening_brackets = "([{"
        closing_brackets = ")]}"
        bracket_pairs = {")": "(", "]": "[", "}": "{"}

        for i in s:
            if i in opening_brackets:
                arr.append(i)
            elif i in closing_brackets:
                if not arr or arr[-1] != bracket_pairs[i]:
                    return False
                arr.pop()
        
        return len(arr) == 0
