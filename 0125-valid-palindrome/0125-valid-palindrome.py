class Solution:
    def isPalindrome(self, s: str) -> bool:        
        s = s.lower()
        res = ""
        for i in s:
            if 'a' <= i <= 'z' or '0'<= i <= '9':
                res += i

        print(res)
    
        i, j = 0, len(s) - 1
        while i < j:
            if i < j and s[i] != s[j]:  # Ensure proper comparison
                return False
            i += 1
            j -= 1

        return True
            
            
        