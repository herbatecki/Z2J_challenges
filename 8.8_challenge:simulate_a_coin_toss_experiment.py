import random

def coin_flip():
    """Randomly return 'heads' or 'tails'."""
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

result = coin_flip()
print(result)

# set at the beginning number of flips as 0
flips = 0
trials_num = 10_000

for trial in range(trials_num):
    if coin_flip() == "heads":
        continue
    else:
        flips += 1

avr_flips_num = flips / trials_num      # average number of flips per trial
print(avr_flips_num)
