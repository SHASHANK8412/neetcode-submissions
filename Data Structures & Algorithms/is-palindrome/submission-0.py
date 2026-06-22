class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()

        temp = ""

        for ch in s:
            if ch.isalnum():
                temp += ch

        if temp == temp[::-1]:
            return True
        else:
            return False