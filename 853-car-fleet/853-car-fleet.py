class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        arr = []
        for p, s in sorted(pairs)[::-1]:
            time = (target - p) / s
            if len(arr) < 1 or len(arr) >= 1 and time > arr[-1]:
                arr.append(time)
        return len(arr)