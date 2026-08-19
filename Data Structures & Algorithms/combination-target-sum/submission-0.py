class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        result = []

        def dfs(start, curr_sum):
            if curr_sum == target:
                result.append(list(path))
                return
            elif curr_sum > target:
                return 

            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i, curr_sum + nums[i])
                path.pop()

        dfs(0, 0)
        
        return result