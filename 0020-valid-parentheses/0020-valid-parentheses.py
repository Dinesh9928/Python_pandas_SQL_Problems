class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s) < 2):
             return False
        st = []
        for i in s:
            if (i == "(" or i== "[" or i == "{"):
                st.append(i)
            elif(i == ")") and st:
                if st[-1]== "(":
                    st.pop()
                else:
                    return False
            elif(i == "]") and st:
                if st[-1]== "[":
                    st.pop()
                else:
                    return False
            elif(i == "}") and st:
                if st[-1]== "{":
                    st.pop()
                else:
                    return False
            else:
                return False
        if not st:
            return True

        return False
            
        