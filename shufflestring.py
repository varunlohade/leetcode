class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        sre = ""
        lst = []
        for i in range(len(indices)):
            lst.append((indices[i],s[i]))
        lst.sort()
        
        for pair in lst:
            sre+=pair[1]
        return sre