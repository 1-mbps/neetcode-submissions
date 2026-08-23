class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        r = 0

        chars = {}
        maxf = 1
        max_length = 1

        while r != len(s):
            if s[r] not in chars:
                chars[s[r]] = 1
            else:
                chars[s[r]] += 1

            maxf = max(maxf, chars[s[r]])

            while (r-l+1) - maxf > k:
                chars[s[l]] -= 1
                l += 1

            max_length = max(max_length, r-l+1)

            r += 1

        return max_length
            
# XYZXX, k=1

# Window 1: X
# Window 2: XY - still valid
# Window 3: XYZ - invalid since num unique keys > k
# Window 4: YZ - valid
# Window 5: YZX - invalid
# Window 6: ZX - valid
# Window 7: ZXX - valid

# ABBBAAAACAA, k=2
# A
# AB
# ABB
# ABBB
# ABBBA
# ABBBAA invalid -> move to BBBAA
# BBBAAA invalid -> move to BBAAA
# BBAAAA
# BBAAAAC invalid -> move to BAAAAC
# BAAAAC

# AABBBB, k=0
# A
# AA
# AAB invalid -> B

# AABBAAB, k=2
            
        