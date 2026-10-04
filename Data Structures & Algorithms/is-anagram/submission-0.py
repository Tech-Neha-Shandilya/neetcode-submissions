class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result=True
        if len(s)!=len(t):
            result=False
            return result
        for m1 in s:
            #result1[m1]=result1.get(0,m1)+1
            if s.count(m1)==t.count(m1):
                continue
            else:
                result=False
                break
        return result


        