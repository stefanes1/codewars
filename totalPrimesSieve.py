#slow solution
def get_total_primes(a, b):
    # a < b < 10^7
    primes = ['2', '3', '5', '7']
    test_list = []
    result = 0
    total_prime = False
    #new (hopefully more efficient) method: create initial loop to first get any prime numbers between a and b
    
    #use sieve of erastosthenes to find primes in range from 2 to b. Then filter out the primes in the range
    #that are less than a
    #is_prime: 1 is prime, 0 is not prime
    is_prime = [1]*b
    #neither 0 or 1 are prime
    is_prime[0] = 0
    is_prime[1] = 0
    i = 2
    while i < int(b**0.5):
        
        #if is_prime[i] = 0, i is already not prime so no need to check its multiples. Increment i by 1 and continue.
        if is_prime[i] == 0:
            i += 1
            continue
        
        #use j as the counter of multiples
        j = 2*i
        while j < b:
            is_prime[j] = 0
            j += i
        i += 1
    
    #final list of primes is every value of 1 in is_prime between is_prime[a] and is_prime[b]
    j = a

    for i in is_prime[a:]:
        string = str(j)

        # test j (every digit of i) against primes list
        
        for k in string:
            if k in primes:
                test_list.append(k)

        if len(test_list) == len(string):
            total_prime = True

        # final check of whether we have a "total prime"
        if total_prime == True and i == 1:
            result += 1

        # change total_prime boolean to false
        total_prime = False

        # make test_list empty again
        test_list = []
        
        #increment j by 1
        j += 1
        
    return result

a = get_total_primes(500,600)

print(a)