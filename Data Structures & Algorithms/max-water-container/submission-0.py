class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights)-1

        m = 0

        while start < end:
            h1 = heights[start]
            h2 = heights[end]
            # print(f"S: {start} E: {end} - vals: {(h1,h2)}")
            if h1 <= h2:
                m = max((end-start)*h1, m)
                start += 1
            else:
                m = max((end-start)*h2, m)
                end -= 1

        return m
        