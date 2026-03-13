class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set=set()
        n=len(nums)
        for i in range(n):
            if nums[i] in hash_set:
                return True
            else:
                hash_set.add(nums[i])
        return False

        