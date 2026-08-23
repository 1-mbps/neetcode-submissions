def index(char: str) -> int:
    return ord(char) - ord('a')

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        letters = [0]*26
        for l in s1:
            letters[index(l)] += 1
        
        for l in range(len(s2)-len(s1)+1):
            r = l+len(s1)
            sub = [0]*26
            for i in range(l,r):
                sub[index(s2[i])] += 1
            
            if sub == letters:
                return True
        
        return False

# lecabee
# le -> X
# ca ->

# lecaabee
# l -> X
# e -> X
# c
# ca
# caa -> a exceeds count -> move left pointer to this position
        

        