class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        out =  {}
        for i in range(len(nums)): 
            difference = target - nums[i]

            if difference in out:
                return [out[difference], i]

            out[nums[i]] = i
            