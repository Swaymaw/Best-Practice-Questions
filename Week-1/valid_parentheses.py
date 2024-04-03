def isValid(s):
    if len(s) < 2:
        return False

    corresponding = {40: 41, 91: 93, 123: 125}
    
    appearance = []
    for i in s:
        if i in ["(", "[", "{"]:
            appearance.append(i)
        else:
            if len(appearance) > 0:
                if corresponding[ord(appearance[-1])] == ord(i):
                    appearance.pop()
                else:
                    return False
            else:
                return False 
    
    if len(appearance) == 0:
        return True 
    else:
        return False
            


print(isValid("[(])"))