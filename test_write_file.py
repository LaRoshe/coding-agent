from functions.write_file import write_file


print("Writing to 'lorem.txt'")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print("==========================================")
print("Writing to 'pkg/morelorem.txt'")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print("==========================================")
print("Writing to '/tmp/temp.txt'")
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
print("==========================================")