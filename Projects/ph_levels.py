# A program that checks whether a pH level is basic, acidic, or neutral.

ph = int(input("Enter the ph value: "))
if ph > 7:
  print("Basic")
elif ph < 7:
  print("Acidic")
else:
  print("Neutral")
