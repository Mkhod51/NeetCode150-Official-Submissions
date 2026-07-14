class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getValue(word: str) -> int:
            primes = [
                2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
                73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
                127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
                179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
                233, 239, 241, 251, 257, 263, 269
                    ]
            val = 1
            for c in word:
                ascVal = ord(c)
                val = val * primes[ord(c) - ord("a")]
            return val 
        
        hm = {}

        for word in strs:
            wordVal = getValue(word) 
            if wordVal in hm:
                hm[wordVal].append(word)
            else:
                hm[wordVal] = [word]
        
        return [lst for lst in hm.values()]


