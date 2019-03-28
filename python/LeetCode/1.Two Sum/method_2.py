#encoding: utf-8

# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        for i in range(l):
            result = target - nums[i]
            if result in nums and nums.index(result) != i:
                return [i,nums.index(result)]


# 执行用时 : 1196 ms, 在Two Sum的Python提交中击败了51.97% 的用户
# 内存消耗 : 12.6 MB, 在Two Sum的Python提交中击败了0.96% 的用户