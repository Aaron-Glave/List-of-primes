import sys
import io
sys.set_int_max_str_digits(100000)
def write_number(primes: [int], numtowrite: int):
        primefile = open("primes.txt", 'a')
        primes.append(numtowrite)
        print(numtowrite, "is prime.")
        primefile.write(str(numtowrite)+'\n')
        primefile.close()

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
	
	for i in range(start, amaximum+1):
		isprime = True
		for prime in primes:
			if i % prime == 0:
				isprime = False
				break
		if isprime:
			write_number(primes, i)	
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
