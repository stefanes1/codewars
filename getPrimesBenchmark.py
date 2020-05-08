import totalPrimes
import gtimeit

bm = gtimeit.Benchmark()

bm.add(totalPrimes.get_total_primes, 500,600)
bm.run(200, multiplicator=100)
