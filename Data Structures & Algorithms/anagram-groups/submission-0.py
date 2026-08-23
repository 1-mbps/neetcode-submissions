class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}
        
        for word in strs:
            srt = ''.join(sorted(word))
            if srt not in d:
                d[srt] = [word]
            else:
                d[srt].append(word)

        return list(d.values())

# initial idea:
# add each letter as key in dictionary
# {"a": "a"}
# {"ac": "ac"}
