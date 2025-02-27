class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        '''
        0,  1, 2, 3,  4
        1, -3, 2, 3, -4

        dp[i] = max abs sum of any subarray ending with nums[i]
        we want max(dp[i])
        dp[0] = 1
        dp[1] = 3
        dp[2] = max(abs(pref[1] + num), abs(num))
        pref[1] = 

        # -7,-1, 0, -2, 1, 3, 8,-2,-6,-1,-10,-6,-6,8,-4,-9,-4,1,4,-9
        # -7,-8,-8,-10,-9,-6, 8, 6, 0,-1,-11
        #                   , 2, 0,-6,-7  
        #  7, 8, 8, 10, 9, 6, 8, 6, 6, 7

        the max positive
        the min negative 
        ending at each index
        '''

        res = 0
        numsLen = len(nums)
        minNeg = [0]
        maxPos = [0]

        for i, num in enumerate(nums):
            minNeg.append(min(num, num + minNeg[i]))
            maxPos.append(max(num, num + maxPos[i]))
            res = max(res, max(abs(minNeg[-1]), abs(maxPos[-1])))

        return res