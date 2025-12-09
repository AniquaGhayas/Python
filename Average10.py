count = 1
total = 0
while count <= 10:
 num = float(input("Enter number {}: ".format(count)))
 total += num
 count += 1
average = total / 10
print("Average of 10 numbers:", average)