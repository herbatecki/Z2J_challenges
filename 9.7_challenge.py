import random

capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
}
# print(capitals_dict.items())

state_choice, capital_choice = random.choice(list(capitals_dict.items()))
# print(state_choice, capital_choice)

while True:
  user_input = input(f"The capital of {state_choice} is: ")
  if user_input.lower() == capital_choice.lower():
    print("Correct")
    break
  else:
    if user_input.lower() == "exit":
      print("Goodbye")
      break
    else:
      print("Try again or quit writing 'exit'")
      continue
