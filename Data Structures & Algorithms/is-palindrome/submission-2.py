class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean_text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
        