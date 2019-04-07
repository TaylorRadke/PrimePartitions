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
    p = [1]
    for i in range(len(primes)):
        if is_prime[i]:
            p.append(primes[i])
    p.append(n)
    return p

def main(n, l = None, u = None):
    primes = sieve(n)
    frontier =  [[i] for i in primes]
    solutions = []

    while len(frontier):
        curr = frontier.pop(0)
        if sum(curr) < n:
            for i in primes:
                cp = list(curr[:])
                cp.append(i)
                cp = tuple(sorted(cp))
                if sum(cp) == n and cp not in solutions:
                    solutions.append(cp)
                elif cp not in frontier:
                    frontier.append(cp)
        
    print(solutions)

if __name__ == "__main__":
    try:
        input_file = sys.argv[1]
        try:
            with open(input_file,"r") as input_file:
                print(input_file.readline())
        except FileNotFoundError:
            print("Error: File {} cannot be found.".format(input_file))
    except IndexError:
        print("Error: A path to file must be provided to read input from.")
            