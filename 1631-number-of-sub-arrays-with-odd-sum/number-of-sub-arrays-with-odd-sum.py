class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        '''
        0, 1, 2
        1, 3, 5

        {
            0: 1, 2
            1: 1
        }

        sum = 0, 1, 4, 5
        res = 0, 1, 2, 4
        sum % 2 = 1 -> look for mod = 1-sum%2 = 0 in dictionary
        '''

        res = 0
        curSum = 0
        modDict = defaultdict(int)
        modDict[0] = 1
        MOD = 10**9 + 7

        for num in arr:
            curSum += num
            res = (res + modDict[1 - curSum % 2]) % MOD
            modDict[curSum % 2] += 1

        return res