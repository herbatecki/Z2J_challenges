universities = [['California Institute of Technology', 2175, 37704],
                ['Harvard', 19627, 39849],
                ['Massachusetts Institute of Technology', 10566, 40732],
                ['Princeton', 7802, 37000], ['Rice', 5879, 35551],
                ['Stanford', 19535, 40569], ['Yale', 11701, 40500],
                ]
##print(universities)

def enrollment_stats(universities):
  students_amount = []
  total_tuition = []
  for university in universities:
    students_amount.append(university[1])
    total_tuition.append(university[2])

  return f"Total students:   {sum(students_amount):,} \nTotal tuition:  $ {sum(total_tuition):,}"


def mean_students(universities):
  students_amount = []
  for university in universities:
    students_amount.append(university[1])
    students_mean = sum(students_amount) / (len(students_amount))

  return students_mean


def mean_tuition(universities):
  total_tuition = []
  for university in universities:
    total_tuition.append(university[2])
    tuition_mean = sum(total_tuition) / (len(total_tuition))

  return tuition_mean


def median_students(universities):
  students_amount = []
  for university in universities:
    students_amount.append(university[1])
    students_amount.sort() # very important cause after making list including number o students we can sort these values
    if len(students_amount) % 2 == 1:
      median_index = int(len(students_amount) / 2)
      median_students = students_amount[median_index]
    else:
      left_center_index = (len(students_amount) - 1) // 2 # floor division to achieve integer as divider
      right_center_index = (len(students_amount) + 1) // 2
      median_students = (students_amount[left_center_index] + students_amount[right_center_index]) / 2 

  return median_students

def median_tuition(universities):
  total_tuition = []
  for university in universities:
    total_tuition.append(university[2])
    total_tuition.sort() # very important
    if len(total_tuition) % 2 == 1:
      median_index = int(len(total_tuition) / 2)
      median_tuition = total_tuition[median_index]
    else:
      left_center_index = (len(total_tuition) - 1) // 2 # floor division to achieve full integer as divider
      right_center_index = (len(total_tuition) + 1) // 2
      median_tuition = (total_tuition[left_center_index] + total_tuition[right_center_index]) / 2

  return median_tuition


##  return f"Total students: {sum(universities[1])} n\ Total tuition: $ {sum(universities[2])}"
print("*"*10)
check = enrollment_stats(universities)
print(check)
print('')
mean_stud = mean_students(universities)
mean_tuit = mean_tuition(universities)
median_stud = median_students(universities)
median_tuit = median_tuition(universities)
print('')
print(f"Student mean:     {mean_stud:,.2f}")
print(f"Student median:   {median_stud:,}")
print('')
print(f"Tuition mean:   $ {mean_tuit:,.2f}")
print(f"Tuition median: $ {median_tuit:,}")
print("*"*10)
