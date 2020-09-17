import math

whole_numbers = 10
floating_point_numbers = 1.1
bunch_of_text = "strings are lots of characters"

name = input("Enter your name:")

my_name = 'Eric Charnesky'
#          0123456789....

print("your name has:", len(name), "characters including spaces")
print("Your first initial is:", name[0])


names = ['Matthew', 'Mark', 'Luke', 'John']
print("whole list of names:", names)
print("second name in the list:", names[1])
names[1] = names[1] + ' Bob'
print("whole list of names:", names)
names.append(name)
print(names)

# square braces for lists
scores = [100, 90, 80, 70, 60, 70, 75, 22, 70]
print('original scores:', scores)
scores[7] += 50
print('modified scores:', scores)
scores.pop(4)
print('modified scores:', scores)
scores.remove(70)
print('modified scores:', scores)

print("min:", min(scores))
print("max:", max(scores))
print("sum:", sum(scores))
print("avg:", sum(scores)/len(scores))

# this will error if the value isn't present - we can fix it after chapter 4
print("a 70 is at index:", scores.index(70))


# parentheses for tuples
scores_two_pull = (100, 90, 80, 70, 60, 70, 75, 22, 70)
print('original scores:', scores_two_pull)

#scores_two_pull[7] += 50
#print('modified scores:', scores_two_pull)
#TypeError: 'tuple' object does not support item assignment

#scores_two_pull.pop(4)
#print('modified scores:', scores_two_pull)
#AttributeError: 'tuple' object has no attribute 'pop'

#scores_two_pull.remove(70)
#print('modified scores:', scores_two_pull)
#AttributeError: 'tuple' object has no attribute 'remove'

print("min:", min(scores_two_pull))
print("max:", max(scores_two_pull))
print("sum:", sum(scores_two_pull))
print("avg:", sum(scores_two_pull)/len(scores_two_pull))

# this will error if the value isn't present - we can fix it after chapter 4
print("a 70 is at index:", scores_two_pull.index(70))

# curly braces for Dictionary type
grade_book = {
    'Matt': 95,
    'Mark': 97,
    'Luke': 100,
    'John': 75
}

print(grade_book)
# lookups by Key in a dictionary
print('Score for John:', grade_book['John'])

# add or update
grade_book['Peter'] = 27
print(grade_book)
grade_book['Peter'] = 97
print(grade_book)
# delete/remove
#del grade_book['John']
grade_book.pop('John')
print(grade_book)

list_of_random_stuff = ['Eric', 10, 89.777, ['E', 'r', 'i', 'c']]

print(list_of_random_stuff[0])
print(list_of_random_stuff[1])
print(list_of_random_stuff[2])
print(list_of_random_stuff[3])

list_of_random_stuff[3].append(' ')
list_of_random_stuff[3].append('C')

print(list_of_random_stuff[3])

print(list_of_random_stuff[0], "got a score of:", list_of_random_stuff[2], "and some bonus:",list_of_random_stuff[1] )

# these do the exact same thing, wow!
print('{} got a score of: {:.2f} and some bonus: {:d}'.format(list_of_random_stuff[0],  list_of_random_stuff[2],  list_of_random_stuff[1]))
print(f'{list_of_random_stuff[0]} got a score of: {list_of_random_stuff[2]:.2f} and some bonus: {list_of_random_stuff[1]:d}')

value = int(input("Enter a number"))
exponent = int(input("Enter an exponent"))

print(f'{value}^{exponent} = {math.pow(value, exponent)}')

