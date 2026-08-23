class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zeroes = 0
        p = 1
        products = []

        for n in nums:
            if n == 0:
                zeroes += 1
            else:
                p *= n
        
        for n in nums:
            if zeroes >= 2 or (zeroes > 0 and n != 0):
                products.append(0)
            elif n == 0:
                products.append(p)
            else:
                products.append(int(p/n))

        return products

        