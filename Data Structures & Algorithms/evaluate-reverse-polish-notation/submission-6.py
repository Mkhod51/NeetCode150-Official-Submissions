class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        print(("-11").isalnum())
        st = []
        for c in tokens:
            try:
                c = int(c)
                st.append(c)
            except ValueError:
                n1 = st.pop()
                n2 = st.pop()
                if c == "+":
                    st.append(n1 + n2)
                elif c == "-":
                    st.append(n2 - n1)
                elif c == "*":
                    st.append(n1 * n2)
                elif c == "/":
                    st.append(int(n2 / n1))
            print(st)
        
        return st[-1]