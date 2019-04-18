from sys import argv
import time

def sieve(n):
    primes = [i for i in range(2,n)]
    is_prime = [True] * len(primes)

    for i in range(len(primes)-1):
        if is_prime[i]:
            for j in range(i+1,len(primes)):
                if i*i <= j:
                    if primes[j] % primes[i] == 0:
                        is_prime[j] = False
    p = [n]
    #Add primes in descending order
    p.extend([primes[(n-2)-1-i] for i in range(len(primes)) if is_prime[(n-2)-1-i]])
    p.append(1)
    return p

def search(slots, total,primes):
    if (slots == 0 and total == 0) or (slots == total):
        return 1
    if total <= 0 and slots != 0 or slots == 0 and total != 0:
        return 0

    solutions = 0
    for i in range(len(primes)):
        solutions += search(slots - 1, total - primes[i], primes[i:])
    return solutions

if __name__ == "__main__":
    input_file = argv[1]
    with open(input_file) as input:
        solve_q = []
        for line in input.readlines():
            line = line.replace("\n","")
            n,*bounds = [int(val) for val in line.split(" ")]
            lower_bound = 1
            upper_bound = n
            if len(bounds) == 1:    lower_bound = upper_bound = bounds[0]
            elif len(bounds) == 2:  lower_bound,upper_bound = bounds

            start = time.time()
            solutions = 0
            for i in range(lower_bound, upper_bound + 1):
                solutions += search(i,n,sieve(n))
                
            print(f"{line}, found {solutions} solutions in, {time.time() - start} seconds")
            solve_q.append(solutions)

        with open("output.txt","w") as output:
            for solution in solve_q:
                output.write(f"{solution}\n")