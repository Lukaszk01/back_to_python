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
