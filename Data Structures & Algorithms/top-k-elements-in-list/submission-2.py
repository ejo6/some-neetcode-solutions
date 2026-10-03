class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # if len(nums) == 1:
        #     return nums

        # 1. Write nums into frequency table
        freq = {}
        buckets = [[] for _ in range(len(nums))]
        result = []

        for num in nums:
            if freq.get(num) is None:
                freq[num] = 1
            else: freq[num] += 1
        
        # 2. Flip frequency table into count/value array
        for key, value in freq.items():
            buckets[value - 1].append(key)
    
        # 3. Run back through buckets
        i = len(buckets) - 1
        j = 0
        while i >= 0 and j < k:
            for num in buckets[i]:
                result.append(num)
                j += 1
            i -= 1


        print(freq)
        print(buckets)    
        return result