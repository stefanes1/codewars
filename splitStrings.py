def solution(s):
    result = []
    #if length of s is 0
    if len(s) == 0:
        return result
    
    #if length of s is even
    elif len(s) % 2 == 0:
        for i in range(1, len(s), 2):
            result.append(s[i-1] + s[i])
        return result
        
    #if length of s is odd
    else:
        for i in range(1, len(s) - 1, 2):
            result.append(s[i-1] + s[i])
        
        result.append(s[-1] + '_')
        return result
    
    pass
