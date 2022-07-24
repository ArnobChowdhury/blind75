class Solution:
    def maxArea(self, height):
        a = 0
        b = len(height) - 1

        max_area = 0

        while a < b:
            min_height = min(height[a], height[b])
            area = min_height * (b - a)

            max_area = max(max_area, area)

            if height[b] <= height[a]:
                b -= 1
            else:
                a += 1

        return max_area


inp = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# ^^^^^^x^^x
# inp = [8, 6, 2, 5, 4, 8, 3, 7]

# inp = [2, 3, 8, 1, 9]
a = Solution()
print(a.maxArea(inp))
