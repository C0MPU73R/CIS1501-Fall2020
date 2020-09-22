import math

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
