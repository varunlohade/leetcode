class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        reverse = str(x)[::-1]
        return x == int(reverse)
        
        
        
#This is a different solution which i submitted initally
# A submission with typical reverse formula is more suitable for such type of programs
