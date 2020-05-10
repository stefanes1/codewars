import totalPrimesSieveOfOdds
import gtimeit

bm = gtimeit.Benchmark()

bm.add(totalPrimesSieveOfOdds.get_total_primes, 500,600)
bm.run(200, multiplicator=100)

