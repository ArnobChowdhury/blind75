class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1

        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res


# a = [3, 4, 5, 1, 2]
# a = [1, 2, 3, 4, 5]
# a = [4, 5, 6, 7, 0, 1, 2]
a = [11, 13, 15, 17]
a = [2, 1]

s = Solution()
min = s.findMin(a)

print(min)
