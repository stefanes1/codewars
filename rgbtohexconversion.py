def rgb(r, g, b):
    #rgb to hex
    # 1s = (1,2,3,4,5,6,7,8,9,A,B,C,D,E,F)
    # 10s = (1,2,3,4,5,6,7,8,9,A,B,C,D,E,F)
    #e.g. 250 = 240 + 10 = 15 * 16 + 10 = FA
    
    #round values
    if r < 0:
    	r = 0 
    
    if g < 0:
    	g = 0
    
    if b < 0:
    	b = 0
    
    if r > 255:
    	r = 255
    
    if g > 255:
    	g = 255
    
    if b > 255:
    	b = 255   
  
    #there is a hex() function
    if r > 15 and g > 15 and b > 15:
        return hex(r)[2:].upper() + hex(g)[2:].upper() + hex(b)[2:].upper()
        
    elif r < 16 and g > 15 and b > 15:
        return "0" + hex(r)[2:].upper() + hex(g)[2:].upper() + hex(b)[2:].upper()

    elif g < 16 and r > 15 and b > 15:
    	return hex(r)[2:].upper() + "0" + hex(g)[2:].upper() + hex(b)[2:].upper()

    elif b < 16 and g > 15 and r > 15:
    	return hex(r)[2:].upper() + hex(g)[2:].upper() + "0" + hex(b)[2:].upper()
    
    elif r < 16 and b < 16 and g > 15:
    	return "0" + hex(r)[2:].upper() + hex(g)[2:].upper() + "0" + hex(b)[2:].upper()
    
    elif r < 16 and b > 15 and g < 16:
    	return "0" + hex(r)[2:].upper() + "0" + hex(g)[2:].upper() + hex(b)[2:].upper()
    	
    elif r > 15 and b < 16 and g < 16:
    	return hex(r)[2:].upper() + "0" + hex(g)[2:].upper() + "0" + hex(b)[2:].upper()
    
    elif r < 16 and b < 16 and g < 16:
    	return "0" + hex(r)[2:].upper() + "0" + hex(g)[2:].upper() + "0" + hex(b)[2:].upper()
    
    else:
    	return 0
