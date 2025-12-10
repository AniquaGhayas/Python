import pandas as pd
import matplotlib.pyplot as plt
filename = input("Enter CSV file name: ")
df = pd.read_csv(filename)
print("Data Loaded:")
print(df)
df.plot(kind="line", title="Line Plot")
plt.show()
df.plot(kind="bar", title="Bar Plot")
plt.show()
df.plot(kind="hist", title="Histogram")
plt.show()
df.plot(kind="box", title="Box Plot")
plt.show()
