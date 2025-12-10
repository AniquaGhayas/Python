#both of these files should remain in the same folder for the module to be imported and used  
#create a module by saving this part of the code as mymodule.py file 

#mymodule.py
def greet(name):
    return "Hello, " + name

#import the mymodule.py file in the main.py file 

#main.py
from mymodule import greet
name = input("Enter your name: ")
print(greet(name))
