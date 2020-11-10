print("example.txt")
file_to_read = open("example.txt")
contents = file_to_read.readlines()
file_to_read.close()
for line in contents:
    print(line, end="")
print()

print("another.txt")
another_file_to_read = open("another.txt")
single_string_contents = another_file_to_read.read()
another_file_to_read.close()
print(single_string_contents)

try:
    oops_file = open("oops.txt")
    oops = oops_file.readlines()
    oops_file.close()
    print(oops)
except FileNotFoundError as exception:
    print(exception)

filename = input("Enter a file name to write:")
file_to_write = open(filename, 'w')
file_to_write.write("print('hello world')")
file_to_write.close()


