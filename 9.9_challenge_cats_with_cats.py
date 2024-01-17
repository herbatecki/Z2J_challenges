cats_list = []

for i in range(100):
  cats_list.append(i + 1)

#print(cats_list)
print()

hats_list = []
for i in range(100):
  hats_list.append("off")

#print(hats_list)
print()

# Python3 code to demonstrate
# conversion of lists to dictionary
# using naive method
# to convert lists to dictionary
make_dict = {}
for cat in cats_list:
  for hat in hats_list:
    make_dict[cat] = hat


def check_hat():  # func with simple logic to reverse current status of hat
  if make_dict[cat] == 'off':
    make_dict[cat] = 'on'
  else:
    make_dict[cat] = 'off'
  return make_dict


for cat in make_dict:  # first check of hats on cats' heads
  check_hat()

print(make_dict)
print()

own_array = []
for i in range(3, 101):  # creating dividers for cats' array
  own_array.append(i)

print(own_array)
print()

for cat in make_dict:  # second step taken by hand to check if func 'check_hat' works
  if cat % 2 == 0:
    #print(f'{cat} and {make_dict[cat]}')
    check_hat()
    #print(f'{cat} and {make_dict[cat]}')

print(make_dict)
print()

for num in own_array:  # loop for continuously dividing cats' array and changing status of cat
  for cat in make_dict:
    if cat % num == 0:
      check_hat()
      continue

print(make_dict)
print()

hat_on = []
hat_off = []
for cat in make_dict:  # loop summarizing hat-on status
  if make_dict[cat] == 'on':
    hat_on.append(cat)
  else:  # summarizing hat-off status
    hat_off.append(cat)

print(f"Cats with hat on head at the end of checking are: {hat_on}")
sum_on = len(hat_on)
print(f"Number of cats with hat on at the end of checkich is {sum_on}")
print()

print(f"Cats with hat on head at the end of checking are: {hat_off}")
sum_off = len(hat_off)
print(f"Number of cats with hat on at the end of checkich is: {sum_off}")
