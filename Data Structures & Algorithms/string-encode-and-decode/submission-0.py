class Solution:
    import re
    #input=aaabbccca->3a2b3c1a

    def encode(self, strs: [str]) -> str:
        result=""
        encode_string="&@#%"
        seperator="_-"
        for s in strs:
            result=result+encode_string+s+seperator
        return result

        

            
    def decode(self, s: str) -> List[str]:
        matches = re.findall(r'&@#%(.*?)_-', s)
        return matches


    
