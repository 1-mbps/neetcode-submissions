class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        products = [[-99,-99] for _ in range(len(nums))]
        p_forward = nums[0]
        p_reverse = nums[-1]

        for i in range(1,len(nums)):
            products[i][0] = p_forward
            p_forward *= nums[i]

        for i in range(len(nums)-2,-1,-1):
            products[i][1] = p_reverse
            p_reverse *= nums[i]

        output = [0]*len(nums)
        output[0] = products[0][1]
        output[-1] = products[-1][0]

        for i in range(1,len(products)-1):
            p1, p2 = products[i]
            output[i] = p1*p2

        return output

        # [1,2,4,6]
        # [(-99,48), (1,24), (2,6), (6,-99)]


        

        