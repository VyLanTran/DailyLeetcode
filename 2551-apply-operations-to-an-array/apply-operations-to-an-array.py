class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        '''
        0,1,2,3,4,5
        1,2,0,0,0,1
        i i i i i i
        size = 0, 1, 2, 3
        if = 0 => size += 1
        else:   
            swap position i with i - size
        '''

        def shiftZeroes(arr):
            numZeroes = 0
            for i in range(len(arr)):
                if arr[i] == 0:
                    numZeroes += 1
                else:
                    arr[i], arr[i - numZeroes] = arr[i - numZeroes], arr[i]

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        shiftZeroes(nums)

        return nums