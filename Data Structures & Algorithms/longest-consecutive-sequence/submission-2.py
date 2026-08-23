class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}

        for n in nums:
            prev = d.get(n-1)
            nxt = d.get(n+1)
            if prev and nxt:
                start = d[n-1][0]
                end = d[n+1][1]

                d[start][1] = end
                d[end][0] = start
                d[n] = [start, end]
            elif prev:
                start = d[n-1][0]
                d[start][1] = n
                d[n] = [start, n]
            elif nxt:
                end = d[n+1][1]
                d[end][0] = n
                d[n] = [n, end]
            else:
                d[n] = [n,n]
        
        if not d:
            return 0
        else:
            return max([end-start+1 for start, end in d.values()])
