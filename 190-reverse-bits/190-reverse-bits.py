class Solution:
    def reverseBits(self, n: int) -> int:
        r = format(n, "b")
        r1 = str(r)[::-1]
        for i in range(len(r), 32):
            r1 += "0"
        
        return int(r1, 2)