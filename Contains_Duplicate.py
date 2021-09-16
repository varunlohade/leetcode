class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _size=len(nums)
        nums.sort()
        for i in range(1,_size):
            if nums[i]==nums[i-1]:
                return True
        return False

# this program calculate duplicate in a array it sorts a array and check if the adjecent elements are same. tried different method but ran into time exceeded