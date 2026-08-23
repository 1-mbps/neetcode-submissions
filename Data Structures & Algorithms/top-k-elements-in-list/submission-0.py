class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for i in nums:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1

        srt = sorted([(v,k) for k,v in counts.items()])

        top_k = srt[-k:]

        return [i[1] for i in top_k]

        