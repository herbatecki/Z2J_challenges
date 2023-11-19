import random

def roll():
    """Randomly return integer from 1 to 6."""
    if random.randint(1, 6) == 1:
        return "1"
    elif random.randint(1, 6) == 2:
        return "2"
    elif random.randint(1, 6) == 3:
        return "3"
    elif random.randint(1, 6) == 4:
        return "4"
    elif random.randint(1, 6) == 5:
        return "5"
    else:
        return "6"

result_of_fair_die = int(roll())
print(result_of_fair_die)

# Starters tallies of random integer equal 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

number_of_rolls = (10_000)
##print(number_of_rolls)

for trial in range(number_of_rolls):
    if roll() == "1":
        one = one + int(roll()) # tutaj myk polega na tym, że w przyroście kroków nie dodaje się jedynie o kolejny krok z zadanego zakresu, tylko o konretnę cyfrę, która została wylosowana spośród 1-6. O jeden krok można dodawać w przypadku układu zerojedynkowego, bo przyrost wynosi tyle ile zadany zakres , natomiast tu może wypaść 4 x 6000, to już suma tego wynosi 24 000.  
    elif roll() == "2":
        two += int(roll())
    elif roll() == "3":
        three += int(roll())
    elif roll() == "4":
        four += int(roll())
    elif roll() == "5":
        five += int(roll())
    else:
        six += int(roll())

"""
print(one)
print(two)
print(three)
print(four)
print(five)
print(six)
"""

average_number_rolled = (int(one) + int(two) + int(three) + int(four) + int(five) + int(six)) / number_of_rolls
#print(average_number_rolled * number_of_rolls)
print(average_number_rolled)

# 8.7 - Simulate Events and Calculate Probabilities
# Solutions to review exercises


from random import randint


# Exercise 1
# Write a function that simulates the roll of a die.
def roll():
    """Return random integer between 1 and 6"""
    return randint(1, 6)


# Exercise 2
# Simulate 10,000 rolls of a die and display the average number rolled.
num_rolls = 10_000
total = 0

for trial in range(num_rolls):
    total = total + roll()

avg_roll = total / num_rolls

#print(total)
print(f"The average result of {num_rolls} rolls is {avg_roll}")
    
