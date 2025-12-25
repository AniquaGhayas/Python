## Since 1927, "The Cyclone" roller coaster has delighted visitors at Coney Island (Brooklyn, NY). 🎢 
##They're now installing a new entry system (the height requirement is 137 cm and the cost is 10 credits) 
##This program helps in filtering out the entries

height = int(input("What is your height(in cms) ? "))
credits = int(input("How many credits do you have ? "))

if height >= 137 and credits >= 10:
  print("Enjoy your ride!")
elif height < 137 and credits >= 10:
  print("You are not tall enough")
elif height >= 137 and credits < 10:
  print("You don't have enough credits")
else:
  print("You don't meet the requirement")
