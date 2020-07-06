from random import randint
guesses_left = 3
# Start your game!
while guesses_left > 0:
  random_number = randint(1, 10)
  print random_number
  guess = int(raw_input("Your guess: "))
  if guess == random_number:
    print "You win!"
    break
    guesses_left -= 1
  else:
    print "You lose"
