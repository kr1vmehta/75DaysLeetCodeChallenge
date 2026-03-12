class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        n=len(nums)
        
        for i in range(n):
            comp=target-nums[i]
            if nums[i] in hash_map:
                return [hash_map[nums[i]],i]
    
            else:
                hash_map[comp]=i
        

        