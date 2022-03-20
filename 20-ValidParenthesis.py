class Solution:
    def isValid(self,s:str) -> bool:
        arr = []
        dict ={
            ")":"(", "}":"{", "]":"["
        }

        for c in s:
            # c will be the key and hence, it's the closing bracket.
            if c in dict:
                # checking if "arr" is not empty and last openning bracket maps related bracket
                if arr and arr[-1] == dict[c]:
                    arr.pop()
                else:
                    return False
            else:
                arr.append(c)

        return True if not arr else False

# s = "[{()}]()"
# s = "()[]{}"
# s = "(]"
# s = "([)]"
# s = "(){}}{"
# s ="()"
# s = "[[[]"

print(Solution.isValid(None, "()"))