def in_order(nums: List[int], p1: int, p2: int) -> bool:
    if not nums:
        return False
    return nums[p1] <= nums[p2]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r) // 2
            print(f"{nums[l:m]} / {nums[m:r+1]}")
            inorder_s1 = in_order(nums, l, m-1)
            inorder_s2 = in_order(nums, m, r)
            if l >= m-1:
                return min(nums[l:r+1])
            if inorder_s1 and inorder_s2:
                print(f"{nums[l]} vs. {nums[m]}")
                if nums[l] <= nums[m]:
                    return nums[l]
                else:
                    return nums[m]
            elif inorder_s1:
                l = m
            elif inorder_s2:
                r = m-1
