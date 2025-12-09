arr = list(map(int, input("Enter numbers: ").split()))
key = int(input("Enter search key: "))
for i, v in enumerate(arr):
    if v == key:
        print("Found at index", i)
        break
else:
    print("Not found")
