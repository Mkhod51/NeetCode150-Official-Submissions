class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = [] 

        for inp in tokens:            
            if inp == "+":
                n1 = st.pop()
                n2 = st.pop()
                st.append(n1+n2)
            
            elif inp == "-":
                n1 = st.pop()
                n2 = st.pop()
                st.append(n2-n1)

            elif inp == "*":
                n1 = st.pop()
                n2 = st.pop()
                st.append(n1*n2)
            
            elif inp == "/":
                n1 = st.pop()
                n2 = st.pop()
                st.append(int(n2 / n1))
            
            else:
                st.append(int(inp))
            

        
        return st[0]