class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        # i = 0
        while l <= r:
            # i += 1
            # if i == 10:
            #     break
            m = (l+r) // 2
            print(f"{nums[l:m]} / {nums[m:r+1]}  - ({l,r})")
            for j in [l,r,m]:
                if nums[j] == target:
                    return j
            if (nums[l] <= nums[m] and nums[l] <= target <= nums[m]) or nums[l] > nums[m]:
                r = m-1
            else:
                l = m+1
        return -1

# case 1: segment 1 is in order, contains target
# case 2: segment 1 not in order


# [3,4,5,6,1,2]
# [3,4,5] / [6,1,2]
# [3,4,5] in order but not included
# [6,1,2] not in order
        