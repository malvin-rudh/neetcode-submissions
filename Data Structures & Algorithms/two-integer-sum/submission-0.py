class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Brute Force Approach:
        Use a for loop to go through each of the nums, then use another for loop to 
        either find if the difference is available in the nums array or if the num
        with an element in the nums array adds up to the target --> O(n^2)

        More Efficient Approach:
        Make a hashmap where the key is the integer in nums itself and the value is a
        list that contains the indexes of the integer appearing in nums. Go through 
        the hashmap using a loop, then for each key, you want to get the complement
        which is (target - key) then try to find it if it appears in the hashmap
        """

        hashmap = {}

        for idx, num in enumerate(nums):
            if num not in hashmap:
                hashmap[num] = []
            hashmap[num].append(idx)

        for key, value in hashmap.items():
            complement = target - key
            if key == complement:
                if len(value) >= 2:
                    return [value[0], value[1]]
            elif complement in hashmap:
                return sorted([value[0], hashmap[complement][0]])


        