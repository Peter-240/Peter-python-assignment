is_raining= True
have_umbrella= False
if is_raining and not have_umbrella:
  print('Stay at home')
elif is_raining and have_umbrella:
  print("You can go outside.")
else:
  print("Enjoy the weather")