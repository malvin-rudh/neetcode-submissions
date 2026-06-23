class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
            Brute Force Approach: 
            Go through each elements of the array and maintain a count hashmap and 
            then go through the count hashmap and if theres any element with count 
            more than 1, then return true

            More Efficient Approach:
            Maintain a hashset, then go through the elements in the array and if 
            any of them is in the hashset, then return true. Else, return false
        """

        dup_set = set()
        
        for num in nums:
            if num in dup_set:
                return True
            else:
                dup_set.add(num)
        return False






















        
        # a = set()

        # for n in nums:
        #     if (n in a):
        #         return True
        #     a.add(n)
        
        # return False