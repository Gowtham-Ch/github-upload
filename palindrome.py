def checkPalindrome(wor):   
    
    wor = wor.lower()
    i = len(wor)
    if i < 2:
        return True
    elif wor[0] == wor[i - 1]:
        return checkPalindrome(wor[1: i - 1]) 
    else:
        return False

val = "mAdAm"
result = checkPalindrome(val) 
if result:
    print("Yes") 
else:
    print("No")