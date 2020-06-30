print "hello world"

january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
october_rainfall = 7.20
november_rainfall = 5.06
december_rainfall = 4.06
september_to_december_rainfall = 5.16 + 7.20 + 5.06 + 4.06

annual_rainfall += september_to_december_rainfall



cucumbers = 100
num_people = 6
whole_cucumbers_per_person = cucumbers / num_people
print whole_cucumbers_per_person


float_cucumbers_per_person = float(cucumbers) / num_people

print float_cucumbers_per_person

haiku = """The old pond,
A frog jumps in:
Plop!"""


float_1 = 0.25
float_2 = 40.0

product = float_1 * float_2

big_string = "The product was " + str(product)



inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

inventory['backpack'].sort()

inventory['backpack'].remove('dagger')
inventory['gold'] += 50

skill_completed = "Python Syntax"

exercises_completed = 13
#The amount of points for each exercise may change, because points don't exist yet
points_per_exercise = 5

point_total = 100

point_total = 100 + exercises_completed * points_per_exercise

print "I got " + str(point_total) +" points!"

"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = 'MONTY'[4]

print fifth_letter

name = "Alex"
quest = "Teaching Python"
color = "Blue"

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." %(name, quest, color)

from datetime import datetime

from datetime import datetime

now = datetime.now()
print now


print '%02d/%02d/%04d' % (now.month, now.day, now.year)

print '%02d/%02d/%04d' % (now.month, now.day, now.year) + ' %02d:%02d:%04d' % (now.hour, now.minute, now.second)

def cube(number):
  return (number * number) * number

def by_three(number):
  if (number % 3 ==0 ):
    return cube(number)
  else:
    return False


    import math
print math.sqrt(25)

minimum = min(1 , 30, -1, -1000)

print minimum
maximum = max(1 , 30, -1, -1000)

print maximum

absolute = abs(-42)

print absolute


print type(22)
print type(1.22)
print type("good")


def shut_down(s):
  if s == "yes":
    return "Shutting down"
  elif s == "no":
    return "Shutdown aborted"
  else:
    return "Sorry"

def distance_from_zero(num):
  if type(num) == int or type(num) == float:
    return abs(num)
  else:
    return "Nope"


def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money

print trip_cost("Los Angeles", 5, 600)




shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

# Write your code below!
def compute_bill(food):
  total = 0
  for item in food:
    if prices[key] > 0:
      total = total + prices[item]
      total / stock[key]
  return total
