import sys
sys.set_int_max_str_digits(100000)
def primes_up_to(amaximum: int):
	primes = []
	try:
		primefile = open("primes.txt", "r")
	except FileNotFoundError:
		print("Creating list...")
		primefile = open("primes.txt", "x")
		primefile.close()
		primefile = open("primes.txt")
		print("File listing primes was created")
	for line in primefile:
		primes.append(int(line))
	primefile.close()
	try:
		start = max(primes)
		print(start)
	except ValueError:
		print("List is empty.")
		start = 2
	
	primefile = open("primes.txt", 'a')
	for i in range(start, amaximum+1):
		isprime = True
		for prime in primes:
			if i % prime == 0:
				isprime = False
				break
		if isprime:
			primes.append(i)
			print(i, "is prime.")
			primefile.write(str(i)+'\n')
	primefile.close()		
	print(primes)
		

if __name__ == '__main__':
	print("Max Prime?")
	done_in = False
	while not done_in:
		try:
			maximum = int(input())
			done_in = True
		except ValueError as e:
			print(e)
		primes_up_to(maximum)