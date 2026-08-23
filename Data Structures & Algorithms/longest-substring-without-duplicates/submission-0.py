# zxyzabyzxc
# z
# zx
# zxy
# zxyz -> xyz
# xyza
# xyzab
# xyzaby -> zaby
# zabyz -> abyz

# xxyx
# x
# x

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        # window
        l = 0
        r = 0
        d = {s[0]: 1}

        # length of longest substring
        m = -1

        while r < len(s)-1:
            r += 1
            d[s[r]] = d.get(s[r],0)+1
            if d[s[r]] > 1:
                while d[s[r]] > 1:
                    d[s[l]] -= 1
                    l += 1
            m = max(r-l+1, m)

        return m

        
        