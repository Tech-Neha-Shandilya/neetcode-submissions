class Solution:
    def isPalindrome(self, s: str) -> bool:

        test_string = "".join(ch for ch in s if ch.isalnum())
        if test_string[len(test_string)-1]=="?":
            test_string=test_string[:-1]

        print(test_string)
        start_index=0
        end_index=len(test_string)-1
        while True:
            if start_index==end_index:
                return True
                break
                

            if test_string[start_index].lower()==test_string[end_index].lower():
                start_index+=1
                end_index-=1
                continue
            else:
                return False
                break


        