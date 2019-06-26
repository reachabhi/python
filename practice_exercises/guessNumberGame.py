import random
realNum = random.randint(1,100)  #73
print(realNum)
guessCount, guessNum = 0, 0
guessList = []
oldGuessDiff = []

while guessNum!=realNum:
	guessNum = int(input("Guess a number between 1-100 \n"))
	guessCount+=1
	guessList.append(guessNum)
	#print(f"Guess count - {guessCount} , Guess List - {guessList}")
	if guessNum==realNum:
		print(f'Found in {guessCount} guesses')
		break
	if guessCount == 1:
		if guessNum<realNum:
			diff = realNum-guessNum
		else:
			diff = guessNum-realNum
		oldGuessDiff.append(diff)
		#print("oldGuessDiff", oldGuessDiff)
		if diff > 10:
			print("cold")
		elif diff <= 10:
			print("warm")
	else:
		if guessNum<realNum:
			diff = realNum-guessNum
		else:
			diff = guessNum-realNum
		#print(diff)
		oldGuessDiff.append(diff)
		#print("oldGuessDiff", oldGuessDiff)
		if diff > 0 or oldGuessDiff[guessCount-2] >0 :
			if diff < oldGuessDiff[guessCount-2]:
				print("warmer")
			else:
				print("colder")
		elif diff < 0 and oldGuessDiff[guessCount-2] >0:
			if diff < oldGuessDiff[guessCount-2]:
				print("colder")
			else:
				print("warmer")

