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
        solutions += search(slots-1, total-primes[i], primes[i:])
    return solutions

def init_search(n, lower_bound = None, upper_bound = None):

    if not upper_bound:
        upper_bound = n

    if not lower_bound:
        lower_bound = 1

    primes = sieve(n)
    start = time.time()
    solutions = 0
    for i in range(lower_bound,upper_bound + 1):
        solutions += search(i,n,primes)
    print(time.time() - start)
    return solutions

if __name__ == "__main__":
    try:
        infile = argv[1]
        try:
            solve_q = []
            with open(infile) as input:
                for line in input.readlines()[:3]:
                    line = line.replace("\n","")
                    vals = [int(val) for val in line.split(" ")]
                    if len(vals) == 1:
                        solutions = init_search(vals[0])
                    elif len(vals) == 2:
                        solutions = init_search(vals[0], vals[1])
                    elif len(vals) == 3:
                        solutions = init_search(vals[0],vals[1],vals[2])
                    else:
                        exit(f"Error: line has too many values\n{line}")
                    solve_q.append(solutions)
            # with open("output.txt","w") as output:
            #     for solution in solve_q:
            #         output.write(solution)
        except FileNotFoundError:
            exit(f"Error: {infile} cannot be found")
    except:
        exit(f"Usage: python {argv[0]} <input file>")