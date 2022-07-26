class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        acc = dict()
        most_freq = 0
        res = 0

        for r in range(len(s)):
            letter = s[r]
            acc[letter] = acc.get(letter, 0) + 1
            most_freq = max(most_freq, acc[letter])

            if (r - l + 1) - most_freq > k:
                left_most = s[l]
                acc[left_most] -= 1
                l += 1

            res = max(res, (r - l + 1))

        return res


s = "AABABBA"
# s = "ABAB"
# s = "AB"

r = Solution()
l = r.characterReplacement(s, 1)
# l = r.characterReplacement(s, 2)
# l = r.characterReplacement(s, 0)

print(l)
