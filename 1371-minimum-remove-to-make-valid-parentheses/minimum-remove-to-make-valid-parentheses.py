class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        list_s = list(s) #make a string to list to avoid immutability
        stack=[] #open parenthesis

        for i,char in enumerate(list_s):
            if char =="(" :
                stack.append(i)
            
            elif  char ==")":
                if stack :
                    stack.pop()
                else:
                    list_s[i] =""
        
        while stack: #extra open parenthesis
            list_s[stack.pop()] = ""
        
        return ''.join(list_s)

        


        