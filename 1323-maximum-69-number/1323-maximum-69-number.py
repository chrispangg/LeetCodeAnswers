class Solution:
    def maximum69Number (self, num: int) -> int:
        numArr = [i for i in str(num)]
        for i, n in enumerate(numArr):
            if n == "6": 
                numArr[i] = "9"
                return int("".join(numArr))
        return num