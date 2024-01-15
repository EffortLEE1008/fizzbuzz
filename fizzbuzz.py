def do_fizzbuzz():

	for i in range(1,21):
		if i % 15 == 0:
			print('fizzbuzz')
		else:
			print(i)


if __name__ == '__main__':
	print(do_fizzbuzz())
