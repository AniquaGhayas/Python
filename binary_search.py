arr = list(map(int, input("Enter sorted numbers: ").split()))
key = int(input("Enter search key: "))
low = 0
high = len(arr) - 1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print("Found at index", mid)
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not found")
