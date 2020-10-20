import math
import random

print("Hi there")

words = 'asdfasdfa asdfg asdf'

print(10+10)


first = 1
second = 2
third = 3
fourth = 4
fifth = 5

if first <= second and third != fourth or fifth == 42:
    print('yeet')


print(words[3])
#words[3] = 'a'


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34]

print(numbers)

# this isn't changing the numbers in the list
for number in numbers:
    number += 1
    # number = number + 1

for index in range(len(numbers)):
    numbers[index] += 1

print(numbers)


def return_multiple():
    return 1, 2


print(return_multiple())


# from https://github.com/EricCharnesky/CIS1501-Fall2019/blob/master/MidtermReview/review.py#L54-L65
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


def difference_of_primes_and_non_primes_through_n( number ):
    sum = 0
    for n in range(1, number+1):
        if is_prime(n):
            sum += n
        else:
            sum -= n
    return sum


def sum_of_primes_in_prime_indexes( some_list ):
    sum = 0
    for index in range(len(some_list)):
        if is_prime(index) and is_prime(some_list[index]):
            sum += some_list[index]
    return sum


def sum_of_values_in_prime_indexes( some_list ):
    sum = 0
    for index in range(len(some_list)):
        if is_prime(index):
            sum += some_list[index]
    return sum


def sum_of_primes_in_list( some_numbers ):
    sum = 0
    for number in some_numbers:
        if is_prime(number):
            sum += number
    return sum


numbers = [ 2,3,4,5 ]

print( sum_of_primes_in_list( numbers ) )


def bad_hash( sentence ):
    total = 0
    for letter in sentence:
        total += ord(letter)
    return total


def verify_hash( sentence, hash_to_check ):
    return hash_to_check == bad_hash(sentence)


def count_vowels(sentence):
    vowel_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in sentence.lower():
        if letter in vowels:
            vowel_count += 1
        if letter == 'y' and random.randint(1, 10) % 2 == 1:
            vowel_count += 1
    return vowel_count


def bad_encryption( some_string ):
    result = []
    for index in range(len(some_string)):
        result.append( ord(some_string[index]) + index )

    return result


def reverse_bad_encryption( some_list ):
    result = ""
    for index in range(len(some_list)):
        result += chr(some_list[index] - index)
    return result


print(bad_encryption("midterm"))
print(reverse_bad_encryption([109, 106, 102, 119, 105, 119, 115]))


def check_if_all_letters_are_in_a_string( letters_to_check_for, string_to_check ):
    for letter in letters_to_check_for:
        if letter not in string_to_check:
            return False
    return True


def ensure_none_of_the_letters_are_in_a_string( letters_to_check_for, string_to_check ):
    for letter in letters_to_check_for:
        if letter in string_to_check:
            return False
    return True

