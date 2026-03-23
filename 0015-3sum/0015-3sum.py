class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        nums.sort()
        for i in range(n-2):
            j=i+1
            k=n-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            else:
                find=-nums[i]
                while j<k:
                    if nums[j]+nums[k]==find:
                        res.append([nums[i],nums[j],nums[k]])
                        j+=1
                        k-=1
                        while j<k and nums[j]==nums[j-1]:
                            j+=1
                        while j<k and nums[k]==nums[k+1]:
                            k-=1
                    elif (nums[j]+nums[k])<find:
                        j+=1
                    else:
                        k-=1
        return res
            
            


               