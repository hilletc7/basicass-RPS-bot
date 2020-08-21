from random import randint

player_name = input("What is your name? >")

def start():

	t = ["Rock", "Paper", "Scissors"]

	computer = t[randint(0,2)]

	player = False

	while player == False:

		player = input("Rock, Paper, Scissors? ")
		if player == computer:
			print("It's a tie!")
		elif player == "Rock":
			if computer == "Paper":
				print("You lose! ", computer, " covers ", format(player),".", " You gotta do better than that, ", format(player_name), ".", sep='')
			else:
				print("You win!", format(player), "smashes", computer)
		elif player == "Paper":
			if computer == "Scissors":
					print("You lose! ", computer, " cuts ", format(player), ".", " You gotta do better than that, ", format(player_name),".", sep='')
			else:
					print("You win!", format(player), "covers", format(player))
		elif player == "Scissors":
			if computer == "Rock":
					print("You lose! ", computer, " smashes ", format(player), ".", " You gotta do better than that, ", format(player_name),".", sep='')
			else:
					print("You win!", format(player), "cut", computer)
		else:
				print("That is not valid, learn to read and try again!")
		restart=input("Would you like to try your luck (Y/N)? >")
		if restart=="Y":
			start()
		else:
			print("Bye")
			exit()

start()
