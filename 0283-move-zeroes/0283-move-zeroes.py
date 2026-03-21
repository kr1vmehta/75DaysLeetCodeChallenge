class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0
        n=len(nums)
        c=0
        for i in range(n):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
            else:
                c+=1
        for i in range(n-c,n):
            nums[i]=0

        