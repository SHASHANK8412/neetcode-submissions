class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            # Opening bracket
            if ch in "([{":
                stack.append(ch)

            # Closing bracket
            else:
                # No opening bracket available
                if not stack:
                    return False

                # Top doesn't match
                if stack[-1] != pairs[ch]:
                    return False

                # Match found
                stack.pop()

        # Valid only if stack is empty
        return len(stack) == 0