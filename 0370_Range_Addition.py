class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0] * length
        for [s, e, inc] in updates:
            arr[s] += inc
            if e + 1 < length:
                arr[e+1] -= inc
        for i in range(1, length):
            arr[i] += arr[i-1]
        return arr
    
    # def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
    #     arr = [0] * (length+1)
    #     for [s, e, inc] in updates:
    #         arr[s] += inc
    #         arr[e+1] -= inc
    #     for i in range(1, length):
    #         arr[i] += arr[i-1]
    #     return arr[:-1]