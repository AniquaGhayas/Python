fname = input("Enter file name: ")
with open(fname, "r") as f:
    text = f.read()
words = text.split()
unique_words = sorted(set(words))
print("Unique words:")
for w in unique_words:
    print(w)
