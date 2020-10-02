import random

magic_number = random.randint(1, 100)

guess = int(input("guess a number from 1-100: "))

max_guess = 10
number_of_guesses = 1

while guess != magic_number and number_of_guesses < 10:

    if guess < magic_number:
        print("too low!")
    else:
        print("too high")

    guess = int(input("guess a number from 1-100: "))
    number_of_guesses += 1

if guess == magic_number:
    print("You guessed it!")
else:
    print("You lose, the number was", magic_number)

#total_score = 0
#number_of_scores = 0
scores = []

score = int(input("enter a score for project 1 or -1 to stop"))
while score != -1:
    #number_of_scores += 1
    #total_score += score
    scores.append(score)
    score = int(input("enter a score for project 1 or -1 to stop"))

print("the average score is: ", sum(scores) / len(scores) )


sentence = input("enter a sentence and I'll count the vowels")
vowels = [ 'A', 'E', 'I', 'O', 'U' ] # or add lower case as well
number_of_vowels = 0

for letter in sentence:
    # use upper if your list only has upper case letters
    if letter.upper() in vowels:
        number_of_vowels += 1

print("your sentence has", number_of_vowels, "vowels")

high_score = 0
low_score = 100

for score in scores:
    if score > high_score:
        high_score = score
    if score < low_score:
        low_score = score

score_adjustment = 100 - high_score

print(scores)

# this is bad if you want to change the original list
for score in scores:
    score += score_adjustment

# if you access the value by index, you can change it
for index in range(len(scores)):
    scores[index] += score_adjustment

print(scores)



print(f"the highest score was {high_score} and the lowest score was {low_score}")


print("watch python print 0-9!")

for value in range(10):
    print(value)


grade_book = {
    'Eric' : 100,
    'Bobby' : 100,
    'Sue' : 100,
    'John' : 90
}

for key in grade_book:
    print(f"{key} has a score of: {grade_book[key]}")


print("TODO - start with nested loops on Thursday")

