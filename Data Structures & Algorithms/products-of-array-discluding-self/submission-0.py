class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post, res = [[1] * len(nums) for _ in range(3)]
        # [1,2,4,6]
        # [1,1,2,8] - pre
        # [48,24,6,1] - post
        # [48,24,12,8] - res

        # [ 0, 1, 2, 3, 4]
        # [-1, 0, 1, 2, 3] - nums
        # [ 1,-1, 0, 0, 0] - pre
        # [ 1,-1, 0, 0, 0] - pre (expected)
        # [ 0, 6, 6, 3, 1] - post
        # [ 0,-6, 0, 0, 0] - res

        # create pre array
        for i in range(1, len(nums)):
            pre[i] = nums[i-1] * pre[i-1]

        # create post array
        for i in range(len(nums)-2, -1, -1):
            post[i] = nums[i+1] * post[i+1]

        for i in range(len(nums)):
            res[i] = pre[i] * post[i]
        
        return res