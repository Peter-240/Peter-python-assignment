score= int(input('Enter your grade: '))
if score>= 80 and score <= 100:
  print(f"Excellent!, your score are {score}")
elif score>= 60 and score <80 :
  print(f"Good!, your score are {score}")
elif score<60:
  print(f'You need improvement, your score is {score}')