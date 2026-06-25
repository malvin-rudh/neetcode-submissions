class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = []
        for idx in range(len(nums)):
            if nums[idx] > 0:
                break ## this is bcs non-zero numbers can't sum up to 0
            
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue

            l, r = idx+1, len(nums)-1
            while (l < r):
                if ((nums[l] + nums[r] + nums[idx]) < 0):
                    l += 1
                elif ((nums[l] + nums[r] + nums[idx]) > 0):
                    r -= 1
                elif ((nums[l] + nums[r] + nums[idx]) == 0):
                    solution.append([nums[idx], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    ## skip duplicate
                    while (l < r) and (nums[l-1] == nums[l]):
                        l += 1
                    while (l < r) and (nums[r] == nums[r+1]):
                        r -= 1
        return solution