class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     acc = dict()
    #     l = 0
    #     res = 0

    #     for r in range(len(s)):
    #         curr = s[r]

    #         if curr in acc and acc[curr] >= l:
    #             l = acc[curr] + 1
    #         acc[curr] = r
            
    #         res = max(res, (r - l + 1))
        
    #     return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        res = 0

        for r in range(len(s)):
            curr = s[r]

            while curr in char_set:
                char_set.remove(curr)
                l += 1 
                
            char_set.add(curr)
            res = max(res, r - l + 1)
        
        return res
            
s = "abcabcbb"
s = "abba"

sol = Solution()
r = sol.lengthOfLongestSubstring(s)
print(r)