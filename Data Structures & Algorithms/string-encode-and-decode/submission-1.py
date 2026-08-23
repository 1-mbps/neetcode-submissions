class Solution:

    def to_3digits(self, num: int) -> str:
        if num >= 100:
            return str(num)
        elif 10 <= num <= 99:
            return f"0{num}"
        else:
            return f"00{num}"

    def encode(self, strs: List[str]) -> str:
        l = self.to_3digits(len(strs))
        lengths = ''.join([self.to_3digits(len(i)) for i in strs])
        return l + lengths + ''.join(strs)

    def decode(self, s: str) -> List[str]:
        l = int(s[:3])
        words = []
        index = 3*(l+1)
        for i in range(1,l+1):
            length = int(s[3*i:(3*i)+3])
            word = s[index:index+length]
            index += length
            words.append(word)
        return words
            
            

