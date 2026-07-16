class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}

        for word in strs:
            freq = [0] * 26

            for char in word:
                index = ord(char) - ord("a")
                freq[index] += 1

            key = tuple(freq)

            if key not in grouped:
                grouped[key] = []

            grouped[key].append(word)

        return list(grouped.values())


strs = [
    "apple",
    "banana",
    "nanaba",
    "leapp",
    "vbwq",
    "vbwq",
    "yyyyyy"
]

sol = Solution()
print(sol.groupAnagrams(strs))