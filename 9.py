def RegExpression(s, p): 
  
    # If pattern is empty 
    if not p: 
        return not s 
  
    # Single character matching 
    if len(p) == 1 or p[1] != '*': 
        if len(s) > 0 and (s[0] == p[0] or p[0] == '.'): 
            return RegExpression(s[1:], p[1:]) 
  
    # Case 2: When the second char of pattern is '*' 
    else: 
        # Iterate over all possible lengths of string 
        i = -1
        while i < len(s) and (i < 0 or p[0] == '.' or p[0] == s[i]): 
            if RegExpression(s[i+1:], p[2:]): 
                return True
            i += 1
    return False
  
# Driver Code 
s = input("Enter the string : ")
p = input("Enter the pattern : ")
print(s,p)
RegExpression(s,p)

