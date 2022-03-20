class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ""

        # Iterate till the Length of the first word
        for i in range(len(strs[0])):
            # for each word
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res

res = Solution.longestCommonPrefix(self=None,strs = ['flower','flow','flight'])
print(res)