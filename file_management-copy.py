##contents of the first file should be copied into the second file

src = input("Enter source file name: ")
dest = input("Enter destination file name: ")
with open(src, "r") as f1:
    data = f1.read()
with open(dest, "w") as f2:
    f2.write(data)
print("File copied successfully.")
