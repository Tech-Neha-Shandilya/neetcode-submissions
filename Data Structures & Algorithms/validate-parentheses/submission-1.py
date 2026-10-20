class Solution:
    def isValid(self, s: str) -> bool:
        result_list=[]
        matching_brackets = {'(': ')','[': ']','{': '}'}
        
        for index in range(0,len(s)):
            
            if s[index] in matching_brackets.keys():
                result_list.append(s[index])
                continue
            
            elif s[index] in matching_brackets.values():
                if index==0:
                    return False
                else:
                    check_bracket=next(k for k, v in matching_brackets.items() if v == s[index])
                    if check_bracket == result_list[-1]:
                        result_list.pop()
                    else:
                        return False
        if len(result_list)!=0:
            return False
        else:
            return True   


        
        