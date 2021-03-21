from random import randint


def compare(choice, comp_choice):
	diff = choice - comp_choice

	ret = 0
	if abs(diff) == 1:
		ret = 1
	elif abs(diff) == 2:
		ret = -1
	ret *= diff and diff/abs(diff)

	return ret


choices_full = ['rock', 'paper', 'scissors']
def print_outcome(choice, comp_choice, outcome):
	print(f'You chose {choices_full[choice]}.')
	print(f'Computer chose {choices_full[comp_choice]}.')
	if outcome == 1:
		print("You won that throw!")
	elif outcome == -1:
		print("You lost that throw!")
	else:
		print("That throw was a tie!")


choices = ['r', 'p', 's']
def throw():
	choice = 0
	cont = True
	while cont:
		try:
			choice = choices.index(input("Enter your move (r/p/s): ").lower()[0])
			cont = False
		except ValueError:
			print("Invalid move. Try again.")
			pass

	comp_choice = randint(0, 2)

	outcome = compare(choice, comp_choice)

	print_outcome(choice, comp_choice, outcome)
	print()

	if outcome == 1:
		return 1, 0
	elif outcome == -1:
		return 0, 1
	else:
		return 0, 0


def main():
	max_wins = 3

	p_wins = 0
	c_wins = 0

	while p_wins < max_wins and c_wins < max_wins:
		p, c = throw()
		if p == 1:
			p_wins += 1
		elif c == 1:
			c_wins += 1
	
	if p_wins == max_wins:
		print("You won the game!")
	else:
		print("You lost the game!")

if __name__ == '__main__':
	main()