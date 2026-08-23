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
            
            
            

# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:

#         m = 1
#         l = 0
#         e = 0

#         # count of most frequent character
#         max_freq = 0

#         # count of other characters
#         other_chars = 0

#         # most frequent character
#         freq_char = s[0]

#         chars = {}

#         while e != len(s)-1:
#             if s[e] not in chars:
#                 chars[s[e]] = 1
#             else:
#                 chars[s[e]] += 1

#             if s[e] == freq_char:
#                 max_freq += 1
#             else:
#                 other_chars += 1
#                 if chars[s[e]] > max_freq:
#                     max_freq = chars[s[e]]
#                     freq_char = s[e]
                
#             if other_chars > k:
#                 s += 1
#                 other_chars -= 1

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
            
        