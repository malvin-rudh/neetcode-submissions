class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []

        def dfs(node, target):
            path.append(node)

            if len(path) == target:
                result.append(list(path))
            else:
                for num in nums:
                    if num not in path:
                        dfs(num, target)
            path.pop()
        
        for num in nums:
            dfs(num, len(nums))
        
        return result