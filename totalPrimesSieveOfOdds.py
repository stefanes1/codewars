# slow solution
def get_total_primes(a, b):
    # a < b < 10^7
    primes = ['2', '3', '5', '7']
    test_list = []
    oddsInRange = []
    result = 0
    total_prime = False

    #NEW new more efficient method. Drastically reduce the number of primes to check by checking only
    #whether all odd numbers in the required range are prime (as opposed to all numbers up to the value of b)
    #1. Calculate all odds in the range

    for i in range(a, b):
        string = str(i)

        # test every digit of i against primes list
        for k in string:
            if k in primes:
                test_list.append(k)

        if len(test_list) == len(string):
            oddsInRange.append(int(string))
            # oddsInList becomes the final list of ints to check

        # make test_list empty again
        test_list = []

    # use sieve of erastosthenes to find primes in the oddsInRange list.
    # is_prime: 1 is prime, 0 is not prime
    is_total_prime = [1] * (len(oddsInRange))

    #start from min value of OddsInRange list

    i=2

    while i < int(b ** 0.5):
        #only execute this code if we KNOW that j is in the OddsInRange list. Otherwise, there's no point. If its
        #in there, we'd like to check whether its prime or not. If it isn't, we sieve it out by changing the value
        #of its index to 0

        #print i=
        #print('i=', i)

        # use j as the counter of multiples
        j = 2*i
        while j < max(oddsInRange):
            j += i
            #print('j=',j)
            if j in oddsInRange:

                is_total_prime[oddsInRange.index(j)] = 0
                #print(is_total_prime)
        i += 1

    # final list of primes is every value of 1 in is_prime between is_prime[a] and is_prime[b]
    return sum(is_total_prime)

