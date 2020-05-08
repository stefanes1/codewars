def derive(coefficient, exponent): 
    
    new_coeff = coefficient * exponent
    
    return str(new_coeff) + 'x^' + str(exponent - 1)
    
