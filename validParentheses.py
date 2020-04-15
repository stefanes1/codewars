def validBraces(string):
    
    #initiate counter to 0
    m = 0
    
    if string[0] in [")","]","}"]:
        print("Closing brace not found")
        return False
    
    #check string forwards
    for i in string:
        if i == "(":
            try:
                print("m to end of string =",string[m:])
                
                n = m + string[m:].index(")")
                
                print("n=",n)
                
                
                #validBraces(string[m:n+1])
            
            except ValueError:
                print("ValueError: closing bracket not found")
                return False
        
        print("m=",m)    
        m+=1
    
    m=0    
    
    #flip string: change "(" to ")" and change ")" to "("
    flippedString = []
    for i in string:
        flippedString.append(0)
        if i == "(":
            flippedString[m] = ")"
        if i == ")":
            flippedString[m] = "("
        m += 1
	    
    #reset counter
    m=0 	
    
    flippedString = "".join(flippedString)
    
    print("string = ",string)
    print("flipped string = ",flippedString)
    
    #reverse string
    reversedString = flippedString[::-1]
    
    print("reversedString = ",reversedString)
    
    #checking reversed string
    print("Checking Reversed String")
    for i in reversedString:
        if i == "(":
            try:
                print("m to end of string =",reversedString[m:])
                
                n = m + reversedString[m:].index(")")
                
                print("n=",n)
                
                
                #validBraces(string[m:n+1])
            
            except ValueError:
                print("ValueError: closing bracket not found")
                return False
        
        print("m=",m)    
        m+=1
    
    
    #print("Hello")
    return True


a = "()"              
b = ")(()))"          
c = "("               
d = "(())((()())())"  

validBraces(d)
