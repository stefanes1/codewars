#fast version of total prime using primePy
from primePy import primes

#slow solution
def get_total_primes(a, b):
    # a < b < 10^7
    primes = ['2', '3', '5', '7']
    test_list = []
    k = 0
    m = 0
    result = 0
    total_prime = False
    for i in range(a, b):
        string = str(i)

        # test j (every digit of i) against primes list
        for j in string:
            if j in primes:
                test_list.append(j)
            if len(test_list) == len(string):
                total_prime = True

        # test whether i is prime number using primePy
        if primes.check(i) == True:
            m += 1

        # final check of whether we have a "total prime"
        if total_prime == True and m == 1:
            result += 1

        # change total_prime boolean to false
        total_prime = False

        # reset m to 0
        m = 0

        # make test_list empty again
        test_list = []

    return result
