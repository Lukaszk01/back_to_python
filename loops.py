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


hobbies = []
hobby = raw_input("Your pick: ")
for hobby in range(3):
  hobbies.append(hobby)
  print hobbies


fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
  if f == 'tomato':
    print 'A tomato is not a fruit!' # (It actually is.)

  print 'A', f
else:
  print 'A fine selection of fruits!'


def digit_sum(n):
  sum = 0
  for i in str(n):
    sum += int(i)
  return sum
print digit_sum(1234)

