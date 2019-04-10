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

def search(n,l = None,u = None):

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
        sum_curr = sum(curr)
        if sum_curr < n:
            for i in primes:
                cp = list(curr[:])
                cp.append(i)
                sum_cp = sum_curr + i
                cp = tuple(sorted(cp))
                if sum_cp == n and cp not in solutions and (len(cp) >= l and len(cp) <= u):
                    solutions.append(cp)
                elif cp not in frontier and len(cp) < u:
                    frontier.append(cp)
        elif curr[0] == n and len(curr) == 1 and 1 >= l and 1 <= u:
            solutions.append(n)

    print(f"n: {n}, solutions: {len(solutions)}, time: {time.time() - start}")
    return len(solutions)

class Node:
    def __init__(self,parent,n):
        self.parent = parent
        self.n = n
        self.children = []
        self.sum_primes = None

        if parent:
            self.parent.children.append(self)

    def __repr__(self):
        string = ""
        for i in self.children:
            string += str(i.n)
            string += "   "
        return string

    @staticmethod
    def create_tree(primes,parent):
        pr_sum = sum_primes(primes,parent.n)
        if pr_sum:
            for res in pr_sum:
                node = Node(parent,res)
                Node.create_tree(primes,node)

mem_primes = dict()
def sum_primes(primes,n):
    if n == 2 or n == 3:
        return (n-1,1)

    if not n in mem_primes:
        for i in primes[-1::-1]:
            for j in primes[-1::-1]:
                if i + j == n:
                    mem_primes[n] = (i,j)
                    return (i,j)

        for i in primes[-1::-1]:
            for j in primes[-1::-1]:
                for k in primes[-1::-1]:
                    if i + j + k == n:
                        mem_primes[n] = (i,j,k)
                        return (i,j,k)
    else:
        return mem_primes[n]

def search_tree(tree,min = None,max = None):
    if min and not max:
        max = tree.n
    elif not min and not max:
        min = 0
        max = tree.n



if __name__ == "__main__":

    n = 11
    a = sieve(n)

    b = dict()
    
    top_lvl = []
    for i in range(len(a)):
        su = []
        for j in range(len(a)):
            if a[i] + a[j] <= n and a[j] <= a[i]:
                su.append(a[i] + a[j])
        if su:
            b[a[i]] = su

    for i in b:
        print(i,b[i])

    # try:
    #     input_file = sys.argv[1]
    #     try:
    #         with open(input_file,"r",encoding="utf-8") as input_file:
    #             with open("output.txt","w") as output_file:
    #                 for line in input_file.readlines():
    #                     line = line.replace("\n","")
    #                     vals = [int(i) for i in line.split(" ")]
                        
    #                     if len(vals) == 1:  sums = search(vals[0])
    #                     elif len(vals) == 2:    sums = search(vals[0],vals[1])
    #                     elif len(vals) == 3:    sums = search(vals[0],vals[1],vals[2])
    #                     else:
    #                         exit(f"Error: Too many positional arguments for line\n{line}")
    #                     output_file.write(str(sums) + "\n")
    #     except FileNotFoundError:
    #         exit(f"Error: File {input_file} cannot be found.")
    # except IndexError:
    #     exit("Error: A path to file must be provided to read input from.")
