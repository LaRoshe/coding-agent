from functions.get_file_content import get_file_content


print("file: lorem.txt")
print(get_file_content("calculator", "lorem.txt"))
print("======")
print("file: main.py")
print(get_file_content("calculator", "main.py"))
print("======")
print("file: pkg/calculator.py")
print(get_file_content("calculator", "pkg/calculator.py"))
print("======")
print("file: bin/cat")
print(get_file_content("calculator", "bin/cat"))
print("======")
print("file: pkg/does_not_exist.py")
print(get_file_content("calculator", "pkg/does_not_exist.py"))
print("======")