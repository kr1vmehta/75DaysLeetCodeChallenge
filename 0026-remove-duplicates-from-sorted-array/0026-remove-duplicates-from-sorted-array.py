class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       
        w=0
        r=1
        for i in range(1,len(nums)):
            if(nums[w]!=nums[r]):
                w+=1
                nums[w]=nums[r]
            r+=1
            
        return w+1
        
        