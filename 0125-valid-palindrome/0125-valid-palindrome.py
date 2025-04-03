class Solution:
    def checkalphanumric(self, ch: str)-> bool:
        return 'a' <= ch <= 'z' or '0'<= ch <= '9'

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i , j = 0 , len(s)-1

        while i < j:
            while( i < j and not self.checkalphanumric(s[i])):
                i += 1
            while(i < j) and not self.checkalphanumric(s[j]):
                j -=1

            if(s[i] != s[j]):
                return False
            i +=1
            j -=1

        return True
            
            
        