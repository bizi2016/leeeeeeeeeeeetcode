class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums

        pivot = random.choice(nums)
        left, mid, right = [], [], []

        for i in nums:
            if i < pivot: left.append(i)
            elif i > pivot: right.append(i)
            else: mid.append(i)
        
        return self.sortArray(left) + mid + self.sortArray(right)
