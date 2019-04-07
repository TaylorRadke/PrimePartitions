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

def main(n,l = None,u = None):
    
    if not l:
        l = 0
        u = n
    elif l and not u:   u = l

    primes = sieve(n)
    frontier =  [[i] for i in primes]
    solutions = []
    start = time.time()

    while len(frontier):
        curr = frontier.pop(0)
        if sum(curr) < n:
            for i in primes:
                cp = list(curr[:])
                cp.append(i)
                cp = tuple(sorted(cp))
                if sum(cp) == n and cp not in solutions and (len(cp) >= l and len(cp) <= u):
                    solutions.append(cp)
                elif cp not in frontier and len(cp) < u:
                    frontier.append(cp)
        elif curr[0] == n and len(curr) == 1 and 1 >= l and 1 <= u:
            solutions.append(n)
    return len(solutions)

if __name__ == "__main__":
    try:
        input_file = sys.argv[1]
        try:
            with open(input_file,"r",encoding="utf-8") as input_file:
                with open("output.txt","w") as output_file:
                    for line in input_file.readlines():
                        line = line.replace("\n","")
                        vals = [int(i) for i in line.split(" ")]
                        if len(vals) == 1:  sums = main(vals[0])
                        elif len(vals) == 2:    sums = main(vals[0],vals[1])
                        elif len(vals) == 3:    sums = main(vals[0],vals[1],vals[2])
                        output_file.write(str(sums) + "\n")
        except FileNotFoundError:
            print("Error: File {} cannot be found.".format(input_file))
    except IndexError:
        print("Error: A path to file must be provided to read input from.")
            