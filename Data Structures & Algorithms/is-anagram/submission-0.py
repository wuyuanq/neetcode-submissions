class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        has = [0] * 26
        hat = [0] * 26

        for i in range(len(s)):
            has[ord(s[i]) - ord('a')] += 1
            hat[ord(t[i]) - ord('a')] += 1

        for i in range(26):
            if has[i] != hat[i]:
                return False

        return True

s = "gggsda"
t = "ggsdag"
sol = Solution()
print(sol.isAnagram(s,t))
