print('hello world!')

order_total = 0
print('order_total type: ', type(order_total))
print('Your order total is: $', order_total)

print("You bought a coffee for $1!")

order_total = order_total + 1
print('order_total type: ', type(order_total))
print('Your order total is: $', order_total)

print("You bought an espresso for $1.50!")

order_total += 1.5

print('order_total type: ', type(order_total))
print('Your order total is: $', order_total)

first_name = 'Eric'
last_name = 'Charnesky'

full_name = first_name + last_name

full_name += " The Great"

print(full_name)

order_total += 1.5

print('order_total type: ', type(order_total))
print('Your order total is: $', order_total)


print('2 to the power of 100', 2.0**100)
print('2 to the power of 200', 2.0**200)
print('2 to the power of 400', 2.0**400)
print('2 to the power of 800', 2.0**800)
#print('2 to the power of 1600', 2.0**1600)
# this is too big!

# format string using a template
print('{:.4f}'.format(1/11))

# int(15/4) makes the result an integer
print('15 divided by 4 is', 15//4, 'remainder', 15 % 4)

print('only a genius can solve this!')
print('9 / 3 * 2')
print('Parentheses Exponents (Multiplication Division Modulus) (Add Sub)')
print(9 / 3 * 2)

some_value = 9
some_value -= 3
some_value *= 2
some_value /= 1
some_value %= 10
print(some_value)

# you can multiply strings
print("hue" * 36)

capital_a = 'A'
print(ord(capital_a))
print(chr(69), chr(82), chr(73), chr(67))
print("I want this on \n\"multiple\" lines")
print('I want this on \n"multiple" lines')
print("Hey, that's my joke!")
print('Hey, that\'s my joke!')
