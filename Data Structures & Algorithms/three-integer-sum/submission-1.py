class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = {}
        triplets = {}

        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        
        for start in range(len(nums)-1):
            for end in range(start+1,len(nums)):
                if start == end:
                    continue
                n1 = nums[start]
                n2 = nums[end]
                diff = 0 - (n1+n2)
                if diff in d:
                    if n1 == diff and d[diff] == 1:
                        continue
                    if n2 == diff and d[diff] == 1:
                        continue
                    if n1 == n2 == diff and d[diff] == 2:
                        continue
                    sorted_lst = sorted([n1,n2,diff])
                    triplets[tuple(sorted_lst)] = True
        
        lst = list(triplets.keys())
        return [list(t) for t in lst]

        