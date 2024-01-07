

noun_list = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verb_list = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adj_list = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prep_list = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverb_list = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

import random

# random_element = random.choices(noun_list, k=3) # generates list of three elements
# random_element = random.choice(noun_list)
# print(random_element)

def adj_choice(list_of_adjectives):
  random_ele = random.choice(adj_list)
  if random_ele[0] == ('a' or 'e' or 'i' or 'o' or 'u' or 'y'):   # nawias ważny dla logiki!
    return f"An {random_ele}"
  else:
    return f"A {random_ele}"

check_adj = adj_choice(adj_list) 
# print(check_adj)


for verb in verb_list:
    verb_rand1 = random.choice(verb_list)
    verb_rand2 = random.choice(verb_list)
    verb_rand3 = random.choice(verb_list)

for noun in noun_list:
  noun_rand1 = random.choice(noun_list)
  noun_rand2 = random.choice(noun_list)
  noun_rand3 = random.choice(noun_list)

for adj in adj_list:
  adj_rand2 = random.choice(adj_list)
  adj_rand3 = random.choice(adj_list)

for prep in prep_list:
  prep_rand1 = random.choice(prep_list)
  prep_rand2 = random.choice(prep_list)

adverb_rand = random.choice(adverb_list)
print()
print(f"{check_adj} {noun_rand1} \
\n{check_adj} {noun_rand1} {verb_rand1} {prep_rand1} the {adj_rand2} {noun_rand2} \
\n{adverb_rand}, the {noun_rand1} {verb_rand2} \
\nthe {noun_rand2} {verb_rand3} {prep_rand2} a {adj_rand3} {noun_rand3}")
