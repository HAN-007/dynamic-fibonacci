def fib(n):
    if(n <= 2):
        return 1
    return fib(n-1) + fib(n -2)

def fastFib(n,memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fastFib(n-1,memo) + fastFib(n-2,memo)
    return memo[n];

print(fastFib(50))# this is a dynamic programing
#print(fib(50))# as you see this is not run enougt fast
