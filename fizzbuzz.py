def do_fizzbuzz():
	
    for i in range(1,21):
		if i % 15 == 0:
			print('fizzbuzz')
		elif i % 5 == 0:
			print('buzz')
        elif i % 3 ==0:
            print('fizz')
		else:
			print(i)


if __name__=='__main__':
    do_fizzbuzz()
