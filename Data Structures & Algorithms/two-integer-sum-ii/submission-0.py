class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
            Brute Force: Use a for loop and for each element go through all the 
            elements after it and check if they sum up to target

            More efficient: Use a 2 ptr approach where l, r = 0, len(numbers). Then, 
            for each time the sum of the 2 pointers is less than the target, move the
            left ptr up by 1, and conversely if sum of 2 ptrs is more than target, 
            move the right ptr down by 1. We would never reach the middle because there
            is only exactly one solution. When the sum of the 2 ptrs are equal to the
            target, then we have found the answer

            Solution works because the array itself is sorted and if the the sum of 2
            ptrs are less than the target, then the only way to increase it is to move
            the left ptr up by 1, same as for the opposite
        """

        l, r = 0, len(numbers) - 1
        while (l < r):
            curr_sum = numbers[l] + numbers[r]
            if (curr_sum) < target:
                l += 1
            elif (curr_sum) > target: 
                r -= 1
            else:
                return [l+1, r+1]
        