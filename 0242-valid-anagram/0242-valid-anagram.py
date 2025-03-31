class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s) != len(t)): # if not equal
            return False
        freq = [0]*26
        for i in s :
            freq[ord(i) - ord('a')] += 1 # ord() to get ASCII value. 

        for j in t:
            freq[ord(j) - ord('a')] -= 1

        for f in freq:
            if f != 0: 
                return False

        return True
        