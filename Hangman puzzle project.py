name = input("======ENTER PLAYERS NAME======= ") 
print("HELLO,", name, "LETS PLAY HANGMAN")
print("HINT : a competition in which you answer questions")
words = ['q','u','i','z']
word=("quiz")
print("Guess the characters : ") 
i = '' 
turns = 10
while turns > 0: 
	p = 0
	for char in words: 
		if char in i: 
			print(char) 	
		else: 
			print("_") 
			p += 1
	if p == 0:  
		print("The word is: ", word)
		print("YOUR SCORE IS = 10")
		print("You Win the first level, Proceed to next level")
		break
	u = input("guess a character:") 
	i += u 
	if u not in words: 
		turns -= 1
		print("Wrong") 
		print("You have", + turns, 'more guesses') 
		if turns == 0: 
			print("You Loose")
print("WELCOME TO NEXT LEVEL")			
print("HINT : a question master")
words = ['q','u','i','z','m','a','s','t','e','r']
word=("quizmaster")
print("Guess the characters : ") 
i = '' 
turns = 10
while turns > 0: 
	p = 0
	for char in words: 
		if char in i: 
			print(char) 	
		else: 
			print("_") 
			p += 1
	if p == 0:  
		print("The word is: ", word)
		print("YOUR SCORE IS = 20")
		print("You Win the second level, Proceed to next level")
		break
	u = input("guess a character:") 
	i += u 
	if u not in words: 
		turns -= 1
		print("Wrong") 
		print("You have", + turns, 'more guesses') 
		if turns == 0: 
			print("You Loose")
print("WELCOME TO NEXT LEVEL")	
print("HINT : helps tp connect distant friend")
words = ['t','e','l','e','p','h','o','n','e']
word=("telephone")
print("Guess the characters : ") 
i = '' 
turns = 10
while turns > 0: 
	p = 0
	for char in words: 
		if char in i: 
			print(char) 	
		else: 
			print("_") 
			p += 1
	if p == 0: 
		print("The word is: ", word)
		print("YOUR SCORE IS = 30")
		print("You Win the third, Proceed to next level")
		break
	u = input("guess a character:") 
	i += u 
	if u not in words: 
		turns -= 1
		print("Wrong") 
		print("You have", + turns, 'more guesses') 
		if turns == 0: 
			print("You Loose")
print("WELCOME TO NEXT LEVEL")
print("HINT : AMERCIAN TV SERIES")
words = ['f','r','i','e','n','d','s']
word=("friends")
print("Guess the characters : ") 
i = '' 
turns = 10
while turns > 0: 
	p = 0
	for char in words: 
		if char in i: 
			print(char) 	
		else: 
			print("_") 
			p += 1
	if p == 0:  
		print("The word is: ", word)
		print("YOUR SCORE IS = 40")
		print("You Win the fourth level, Proceed to next level")
		break
	u = input("guess a character:") 
	i += u 
	if u not in words: 
		turns -= 1
		print("Wrong") 
		print("You have", + turns, 'more guesses') 
		if turns == 0: 
			print("You Loose")
print("WELCOME TO NEXT LEVEL")
print("HINT : peter pan")
words = ['t','i','n','k','e','r','b','e','l','l']
word=("tinkerbell")
print("Guess the characters : ") 
i = '' 
turns = 10
while turns > 0: 
	p = 0
	for char in words: 
		if char in i: 
			print(char) 	
		else: 
			print("_") 
			p += 1
	if p == 0:  
		print("The word is: ", word)
		print("YOUR SCORE IS = 50")
		print("You Win the fifth level, Proceed to next level")
		break
	u = input("guess a character:") 
	i += u 
	if u not in words: 
		turns -= 1
		print("Wrong") 
		print("You have", + turns, 'more guesses') 
		if turns == 0: 
			print("You Loose")
print("WELCOME TO NEXT LEVEL")
print("HINT : GAME")
words = ['c','r','i','c','k','e','t']
word=("cricket")
print("Guess the characters : ") 
i = '' 
turns = 10
while turns > 0: 
	p = 0
	for char in words: 
		if char in i: 
			print(char) 	
		else: 
			print("_") 
			p += 1
	if p == 0:  
		print("The word is: ", word)
		print("YOUR SCORE IS = 60")
		print("You Win the sixth level, Proceed to next level")
		break
	u = input("guess a character:") 
	i += u 
	if u not in words: 
		turns -= 1
		print("Wrong") 
		print("You have", + turns, 'more guesses') 
		if turns == 0: 
			print("You Loose")

print("WELCOME TO NEXT LEVEL")
print("HINT : royal enfield trip")
words = ['l','e','h','l','a','d','a','k','h']
word=("leh ladakh")
print("Guess the characters : ") 
i = '' 
turns = 10
while turns > 0: 
	p = 0
	for char in words: 
		if char in i: 
			print(char) 	
		else: 
			print("_") 
			p += 1
	if p == 0: 
		print("The word is: ", word)
		print("YOUR SCORE IS = 70")
		print("You Win the seventh level, Proceed to next level")
		break
	u = input("guess a character:") 
	i += u 
	if u not in words: 
		turns -= 1
		print("Wrong") 
		print("You have", + turns, 'more guesses') 
		if turns == 0: 
			print("You Loose")
print("WELCOME TO NEXT LEVEL")
print("HINT : RELATED TO PYRAMID")
words = ['s','p','h','i','n','x']
word=("sphinx")
print("Guess the characters : ") 
i = '' 
turns = 6
while turns > 0: 
	p = 0
	for char in words: 
		if char in i: 
			print(char) 	
		else: 
			print("_") 
			p += 1
	if p == 0: 
		print("The word is: ", word)
		print("YOUR SCORE IS = 80")
		print("You Win the eighth level, Proceed to next level")
		break
	u = input("guess a character:") 
	i += u 
	if u not in words: 
		turns -= 1
		print("Wrong") 
		print("You have", + turns, 'more guesses') 
		if turns == 0: 
			print("You Loose")
print("WELCOME TO NEXT LEVEL")
print("HINT : a feeling of state or happiness")
words = ['n','i','r','v','a','n','a']
word=("nirvana")
print("Guess the characters : ") 
i = '' 
turns = 10
while turns > 0: 
	p = 0
	for char in words: 
		if char in i: 
			print(char) 	
		else: 
			print("_") 
			p += 1
	if p == 0:  
		print("The word is: ", word)
		print("YOUR SCORE IS = 90")
		print("You Win the ninth level, Proceed to next level")
		break
	u = input("guess a character:") 
	i += u 
	if u not in words: 
		turns -= 1
		print("Wrong") 
		print("You have", + turns, 'more guesses') 
		if turns == 0: 
			print("You Loose")
print("WELCOME TO NEXT LEVEL")
print("HINT : band")
words = ['l','i','n','k','i','n','p','a','r','k']
word=("linkin park")
print("Guess the characters : ") 
i = '' 
turns = 10
while turns > 0: 
	p = 0
	for char in words: 
		if char in i: 
			print(char) 	
		else: 
			print("_") 
			p += 1
	if p == 0:  
		print("The word is: ", word)
		print("YOUR SCORE = 100")
		print("CONGRATS YOU HAVE WON THE GAME >_<") 
		break
	u = input("guess a character:") 
	i += u 
	if u not in words: 
		turns -= 1
		print("Wrong") 
		print("You have", + turns, 'more guesses') 
		if turns == 0: 
			print("You Loose")
			
print("WELCOME TO NEXT LEVEL")
print("HINT : A LEARNING HOME WHERE WHE CAN LEARN FASTER AND BETTER")
words = ['t','e','c','h','b','o','o','s','t','e','r']
word=("techbooster")
print("Guess the characters : ") 
i = '' 
turns = 10
while turns > 0: 
	p = 0
	for char in words: 
		if char in i: 
			print(char) 	
		else: 
			print("_") 
			p += 1
	if p == 0:  
		print("The word is: ", word)
		print("YOUR SCORE IS 110 on 110, EXCELLENT")
		print("CONGRATS YOU HAVE WON THE GAME >_<") 
		break
	u = input("guess a character:") 
	i += u 
	if u not in words: 
		turns -= 1
		print("Wrong") 
		print("You have", + turns, 'more guesses') 
		if turns == 0: 
			print("You Loose")
