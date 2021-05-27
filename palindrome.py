def isPal(s):

    #s is the string to evaluate, will be passed to us as a parameter

    for i in range(len(s)//2):
        # will go halfway of the word
        print("Comparing",s[i],"and",s[-(i+1)])
        if s[i] == s[-(i+1)]:
            continue
        else:
            return False

    return True
    
    
