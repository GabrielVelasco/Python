class Solution:
    def sumArray(self, arr) -> int:
        # O(n)

        acum = 0
        for k in arr:
            acum += k
        
        return acum

    def maxSubArray_N3(self, nums) -> int:
        # O(N³)

        ans = 0
        for i in range(0, len(nums)): # n
            for j in range(i, len(nums)): # n
                # soma de arr[i:j]
                ans = max(ans, self.sumArray(nums[i:j+1])) # n
        
        return ans

    ##############################################################

    def cumSum(self, nums):
        # faz 'acumulacao' de um array
        # permite fazer sum(arr[i:j]) em tempo constante
        # O(n)

        # construindo o vetor acumulado
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]

    def maxSubArray_cumSum(self, nums) -> int:
        # nova complexidade == O(n²)

        self.cumSum(nums)

        ans = 0
        for i in range(0, len(nums)): # n
            for j in range(i, len(nums)): # n
                # soma de arr[i:j]
                if i > 0:
                    ans = max(ans, nums[j] - nums[i-1]) # soma no intervalo arr[i:j]
                else:
                    ans = max(ans, nums[j])

        return ans