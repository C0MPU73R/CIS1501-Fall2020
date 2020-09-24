import math
import random

credits_remaining = int(input("How many more credits do you need?"))

cost_per_credit = int(input("How much does 1 credit cost"))

credits_per_semester = int(input("How many credits do you take per semester?"))

number_of_remaining_semesters = math.ceil(credits_remaining / credits_per_semester)

credits_remaining_in_last_semester = credits_remaining % credits_per_semester

cost_per_semester = credits_per_semester * cost_per_credit

if credits_per_semester >= 12:
    cost_per_semester = 12 * cost_per_credit

if credits_remaining_in_last_semester == 0:
    total_cost = cost_per_semester * number_of_remaining_semesters
else:
    total_cost = cost_per_semester * (number_of_remaining_semesters - 1)
    total_cost += credits_remaining_in_last_semester * cost_per_credit

print(f"It will cost ${total_cost:,.0f} + fees and books")

score = float(input("enter your percentage score ( 0 - 100 ):"))

if score < 60:
    print("E")
elif score < 64:
    print("D-")
elif score < 67:
    print("D")
elif score < 70:
    print("D+")
elif score < 74:
    print("C-")
elif score < 77:
    print("C")
elif score < 80:
    print("C+")
elif score < 84:
    print("B-")
elif score < 87:
    print("B")
elif score < 90:
    print("B+")
elif score < 94:
    print("A-")
elif score <= 100:
    print("A")
else:
    print("That's not a valid score, did you cheat?")
    answer = input("Well, did you?")
    if answer.lower() == 'yes':
        print("You fail!")
    else:
        print("Wow, you must work really hard!")


if score < 60:
    print("E")
if 60 <= score < 64:
    print("D-")
if 64 <= score < 67:
    print("D")
if 67 <= score < 70:
    print("D+")
if 70 <= score < 74:
    print("C-")
if 74 <= score < 77:
    print("C")
if 77 <= score < 80:
    print("C+")
if 80 <= score < 84:
    print("B-")
if 84 <= score < 87:
    print("B")
if 87 <= score < 90:
    print("B+")
if 90 <= score < 94:
    print("A-")
if 94 <= score <= 100:
    print("A")
if score > 100:
    print("That's not a valid score, did you cheat?")


name = input("Enter your name")
if name.lower() == "eric":
    print("Can we be done yet?")
else:
    print("Pay more attention!")


print("On Thursday, start with section 4.5 - boolean operators and membership operators")
print("Don't forget the conditional operator")

is_ready_for_class = True

if is_ready_for_class:
    print("Start taking notes?")

age = int(input("How old are you?"))
yearly_income = int(input("What's your yearly income?"))

if age >= 18 and yearly_income >= 24000:
    print("Here's your debt machine!")
else:
    print("Too risky!")

if age >= 35 or yearly_income >= 60000:
    print("Here's your debt machine!")
else:
    print("Too risky!")


specials = ['Ham Sandwich', 'Turkey Soup', 'Chili']
menu = {
    'Ham Sandwich': 3.5,
    'Turkey Soup': 3,
    'Chili': 2,
    'Hot Dog': 1,
    'Coffee': 1.5
}

order = input("What do you want to buy from our amazing shop?")


order_total = 0

if order not in menu:
    print("We don't sell that!")
else:
    order_total = menu[order]

    if order in specials:
        order_total -= .5

    print("Enjoy your", order, "your cost is: $", order_total)

name = 'Eric'
your_name = input("Enter your name")
another_name = your_name

print( name is your_name )
print( "id(name)", id(name))
print( "id(your_name)", id(your_name))
print( "id(another_name)", id(another_name))

your_name = 'Eric C'
print( "id(your_name)", id(your_name))
print( "id(another_name)", id(another_name))

print("Please excuse my modulus dear aunt sally!")
print( 12 / 3 * 2 )


temp = int(input("What's the temp?"))
#if temp > 50:
#    legwear = "shorts"
#else:
#    legwear = "pants"

legwear = "shorts" if temp > 50 else "pants"

print("based on the weather, you should wear", legwear)

print(random.randint(0, 9))
print(random.randint(0, 9))
print(random.randint(0, 9))
print(random.randint(0, 9))
print(random.randint(0, 9))
print(random.randint(0, 9))
print(random.randint(0, 9))
print(random.randint(0, 9))
print(random.randint(0, 9))
print(random.randint(0, 9))
print(random.randint(0, 9))

# 5 5 5 5 - winning numbers
# 5 5 5 4
# 5 5 5 6
# 5 5 4 5
# 5 5 6 5
# 5 4 5 5
# 5 6 5 5
# 4 5 5 5
# 6 5 5 5
