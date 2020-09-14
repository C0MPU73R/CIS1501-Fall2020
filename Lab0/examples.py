import math

print("Hello world")

name = input("Enter your name: ")
print(name)

cups_of_coffee = float(input(name + ", how many cups of coffee have you drank?\n"))

# https://www.healthline.com/nutrition/how-much-caffeine-in-coffee
total_mg_of_caffeine = cups_of_coffee * 95

total_caffeine_rounded_up = math.ceil(total_mg_of_caffeine)

print(name + ", you have consumed", total_caffeine_rounded_up, "mgs of caffeine")