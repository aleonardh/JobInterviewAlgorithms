# Written by JGFM4
# Last update: 2018-02-20

for i in range(1,101):
	if i % 15 == 0:
		print("FizzBuzz")
	
	elif i % 3 == 0:
		print("Fizz")

	elif i % 5 == 0:
		print("Buzz")

	else:
		print(i)
