def fib(n):
	if n <= 1:
		return n
	return fib(n-1) + fib(n-2)
def countWays(s):
	return fib(s + 1)
print("enter the value of s by user:")
s=int(input())
print ("Number of ways = ")
print (countWays(s))
