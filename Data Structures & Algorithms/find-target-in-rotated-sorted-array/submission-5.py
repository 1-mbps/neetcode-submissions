class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r) // 2
            for j in [l,r,m]:
                if nums[j] == target:
                    return j
            if (nums[l] <= nums[m] and nums[l] <= target <= nums[m]) or nums[l] > nums[m]:
                r = m-1
            else:
                l = m+1
        return -1

# case 1: segment 1 is in order, contains target -> check segment 1
# case 2: segment 1 is in order, does not contain target -> check segment 2
# case 3: segment 1 not in order, possibly contains target -> check segment 2
        