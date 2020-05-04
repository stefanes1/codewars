def generate_hashtag(s):
    
    if len(s) == 0 or len(s) > 140:
        return False
    
    
    else:
        
        #trim whitespace and create capitalized list
        capitalized = []
        for i in s.split():
            capitalized.append(i.capitalize())
        
        #join together
        joined = ''.join(capitalized)
        hashtag = '#' + joined
        return hashtag
