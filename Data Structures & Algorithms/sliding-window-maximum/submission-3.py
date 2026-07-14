import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        res = [0] * (n - k + 1)

        heap = []
        for i in range(k):
            heap.append((-nums[i], i))

        heapq.heapify(heap)
        res[0] = heap[0][0] * -1

        for r in range(k, n):
            l = r - k + 1
            heapq.heappush(heap, (-nums[r], r))
            while (heap and heap[0][1] < l):
                heapq.heappop(heap)
            res[l] = heap[0][0] * -1

        return res
        