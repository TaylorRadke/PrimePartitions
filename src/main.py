import sys
import time

def sieve(n):
    primes = [i for i in range(2,n)]
    is_prime = [True] * len(primes)

    for i in range(len(primes)-1):
        if is_prime[i]:
            for j in range(i+1,len(primes)):
                if primes[j] % primes[i] == 0:
                    is_prime[j] = False
    p = [prime for i,prime in enumerate(primes) if is_prime[i]]
    p.insert(0,1)
    p.append(n)
    return p


def search(n,primes):
    return [[i,n-i] for i in range(n) if i <= n-i and i in primes]


if __name__ == "__main__":
    n = int(sys.argv[1])
    primes= sieve(n)

    result = search(n,primes)

    frontier = []

    frontier.extend(result)
    solutions = []

    while frontier:
        curr = frontier.pop(0)
        print(curr)
        if all(val in primes for _,val in enumerate(curr)) and curr not in solutions:
            solutions.append(curr)
        for i in curr:
            if i > 1:
                new = search(i,primes)
                for j in new:
                    cp = curr[:]
                    cp.remove(i)
                    cp.extend(j)
                    frontier.append(sorted(cp))
    print(solutions)
    print(len(solutions))