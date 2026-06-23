import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
            Go through each element in nums and create a freq dictionary, then use a
            min-heap to store the first k elements, and go through the remaining
            (n - k) elements in the nums array, and pop & swap if the element is 
            greater than the top element in the array. This is to keep the top k most
            largest elements always in the heap and compare the least one in the heap
        """

        freq_dict = {}

        ## build the frequency dictionary
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        ## Min-Heap:
        # heap = []
        # for key, val in freq_dict.items():
        #     heapq.heappush(heap, (val, key))

        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # return [item[1] for item in heap]

        ## Bucket sort:
        bucket = [[] for i in range(len(nums) + 1)] 
        for key, val in freq_dict.items():
            bucket[val].append(key)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res




        



        