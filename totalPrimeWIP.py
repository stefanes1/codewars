def get_total_primes(a, b):
    #a < b < 10^7
    primes = ['2','3','5','7']
    test_list = []
    k=0
    m=0
    result = 0
    total_prime = False
    for i in range(a,b):
        string = str(i)
        
        #test j (every digit of i) against primes list
        for j in string:
            if j in primes:
                test_list.append(j)
            if len(test_list) == len(string):
                total_prime = True
            

        for l in range (2,i):
            if i%l != 0:
                m += 1
            
        #final check of whether we have a "total prime"
        if total_prime == True and m == i/2  - 1:
            result += 1
        
        total_prime = False
    
    return result
        
            
                
    # Happy coding!
    
a = get_total_primes(10,100)
print(a)
