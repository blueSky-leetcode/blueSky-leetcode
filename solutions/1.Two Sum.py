class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i in range(len(nums)):
            component = target - nums[i]
            if component in result:
                return [result[component], i]
            result[nums[i]] = i
        