from functions.get_files_info import get_files_info

print(f'dir: "."')
print(get_files_info("calculator", "."))
print("=======")
print(f'dir: "pkg"')
print(get_files_info("calculator", "pkg"))
print("=======")
print(f'dir: "/bin"')
print(get_files_info("calculator", "/bin"))
print("=======")
print(f'dir: "../"')
print(get_files_info("calculator", "../"))
print("=======")

