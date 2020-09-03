print('Hello world!')

string_input = input("Please enter a temperature in F")
temp_in_f = int(string_input)
temp_in_c = (temp_in_f - 32) * 5 / 9

# using a variable we haven't declared and given a value will give an error
#print(temp_IN_c)
print(temp_in_c)
