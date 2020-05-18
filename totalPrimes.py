#final solution
def get_total_primes(a, b):

    #PART 1 - find primes - what follows is a fast routine to find the prime numbers between a and b, copied from stack overflow, here:
    #https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
    """ Returns  a list of primes a <= prime < b """
    sieve = [True] * int((b / 2))
    for i in range(3, int(b ** 0.5) + 1, 2):
        if sieve[int(i / 2)]:
            sieve[int(i * i / 2)::i] = [False] * (int((b - i * i - 1) / (2 * i)) + 1)
    primes_in_range = [2] + [2 * i + 1 for i in range(1, int(b / 2)) if sieve[i] and (2 * i + 1) >= a]
    
    #initialize result to length of primes_in_range
    if a >= 2:
        result = len(primes_in_range) - 1
    else:
        result = len(primes_in_range)
    
    #list of prime numbers between 1 and 10, as strings
    primes = ['2','3','5','7']
    
    #check whether we have a "total" prime. I.e. whether all digits of the prime number are also prime
    for k in primes_in_range:
        for l in str(k):
            if l not in primes:
                result -= 1
                break
                
    return result
