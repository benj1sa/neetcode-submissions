class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post, res = [[1] * len(nums) for _ in range(3)]

        # create pre array
        for i in range(1, len(nums)):
            pre[i] = nums[i-1] * pre[i-1]

        # create post array
        for i in range(len(nums)-2, -1, -1):
            post[i] = nums[i+1] * post[i+1]

        for i in range(len(nums)):
            res[i] = pre[i] * post[i]
        
        return res