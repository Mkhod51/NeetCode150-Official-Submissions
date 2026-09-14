class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            newSubsets = []
            for ss in res:
                newSubsets.append(ss + [n])

            res.extend(newSubsets)


        return res