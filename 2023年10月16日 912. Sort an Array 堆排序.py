class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        for i in range(n, -1, -1):
            self.heapify(i, n, nums)
        
        for i in range(n-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(0, i, nums)
        
        return nums
    
    def heapify(self, i, n, nums):

        left = i*2 + 1
        right = i*2 + 2
        largest = i

        if left < n and nums[left] > nums[largest]: 
            largest = left
        if right < n and nums[right] > nums[largest]: 
            largest = right
        
        if largest != i:
            nums[largest], nums[i] = nums[i], nums[largest]
            self.heapify(largest, n, nums)
