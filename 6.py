# from datetime import datetime

# def add_journal_entry():
#     entry = input("Enter your journal entry: ")
#     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     with open("journal.txt", "a") as f:
#         f.write(f"{now}\n{entry}\n\n")

# # Пример вызова:
# add_journal_entry()




# def read_and_analyze_journal():
#     try:
#         with open("journal.txt", "r") as f:
#             content = f.read()
#             entries = content.strip().split("\n\n")
#             print(f"Number of entries: {len(entries)}")
#             if entries:
#                 print("Most recent entry:")
#                 print(entries[-1])
#             else:
#                 print("No entries found.")
#     except FileNotFoundError:
#         print("journal.txt not found.")

# # Пример вызова:
# read_and_analyze_journal()




# import os

# def file_manager():
#     while True:
#         print("\nFile Manager Menu:")
#         print("1. Create a new file")
#         print("2. List files in current directory")
#         print("3. Delete a file")
#         print("4. Exit")

#         choice = input("Choose an option (1-4): ")

#         if choice == '1':
#             filename = input("Enter new file name: ")
#             with open(filename, "w") as f:
#                 f.write("")  # создаём пустой файл
#             print(f"File '{filename}' created.")
#         elif choice == '2':
#             files = os.listdir('.')
#             print("Files in current directory:")
#             for file in files:
#                 print(f" - {file}")
#         elif choice == '3':
#             filename = input("Enter file name to delete: ")
#             if os.path.exists(filename):
#                 confirm = input(f"Are you sure you want to delete '{filename}'? (yes/no): ")
#                 if confirm.lower() == 'yes':
#                     os.remove(filename)
#                     print(f"File '{filename}' deleted.")
#                 else:
#                     print("Delete cancelled.")
#             else:
#                 print(f"File '{filename}' does not exist.")
#         elif choice == '4':
#             print("Exiting file manager.")
#             break
#         else:
#             print("Invalid option. Please try again.")

# # Пример вызова:
# # file_manager()



# import os

# def list_directories_files(path):
#     dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
#     files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
#     all_items = os.listdir(path)

#     print(f"Directories in '{path}': {dirs}")
#     print(f"Files in '{path}': {files}")
#     print(f"All contents in '{path}': {all_items}")

# # Example
# list_directories_files(".")



# def check_access(path):
#     print(f"Exists: {os.path.exists(path)}")
#     print(f"Readable: {os.access(path, os.R_OK)}")
#     print(f"Writable: {os.access(path, os.W_OK)}")
#     print(f"Executable: {os.access(path, os.X_OK)}")

# # Example
# check_access(".")



# def path_info(path):
#     if os.path.exists(path):
#         print(f"Path exists: {path}")
#         print(f"Directory part: {os.path.dirname(path)}")
#         print(f"File part: {os.path.basename(path)}")
#     else:
#         print(f"Path does not exist: {path}")

# # Example
# path_info("example.txt")




# def count_lines(filename):
#     try:
#         with open(filename, "r") as f:
#             lines = f.readlines()
#             print(f"Number of lines in {filename}: {len(lines)}")
#     except FileNotFoundError:
#         print(f"{filename} not found.")

# # Example
# count_lines("example.txt")




# def write_list_to_file(filename, data_list):
#     with open(filename, "w") as f:
#         for item in data_list:
#             f.write(f"{item}\n")
#     print(f"List written to {filename}")

# # Example
# write_list_to_file("list_output.txt", ["apple", "banana", "cherry"])




# import string

# def create_alphabet_files():
#     for letter in string.ascii_uppercase:
#         filename = f"{letter}.txt"
#         with open(filename, "w") as f:
#             f.write(f"This is file {filename}\n")
#     print("Files A.txt to Z.txt created.")

# # Example
# create_alphabet_files()




# def copy_file(src, dest):
#     try:
#         with open(src, "r") as f_src, open(dest, "w") as f_dest:
#             for line in f_src:
#                 f_dest.write(line)
#         print(f"Copied from {src} to {dest}")
#     except FileNotFoundError:
#         print(f"Source file {src} not found.")

# # Example
# copy_file("example.txt", "copy_of_example.txt")




# def delete_file(path):
#     if os.path.exists(path):
#         if os.access(path, os.W_OK):
#             os.remove(path)
#             print(f"Deleted file: {path}")
#         else:
#             print(f"No write permission to delete: {path}")
#     else:
#         print(f"File does not exist: {path}")

# # Example
# delete_file("file_to_delete.txt")




# from functools import reduce
# import math
# import time

# # 1. Multiply all the numbers in a list
# def multiply_list(numbers):
#     return reduce(lambda x, y: x * y, numbers)

# # 2. Count uppercase and lowercase letters in a string
# def count_case(s):
#     upper_count = sum(1 for c in s if c.isupper())
#     lower_count = sum(1 for c in s if c.islower())
#     print(f"Uppercase letters: {upper_count}")
#     print(f"Lowercase letters: {lower_count}")

# # 3. Check if string is palindrome
# def is_palindrome(s):
#     cleaned = ''.join(c.lower() for c in s if c.isalnum())
#     return cleaned == cleaned[::-1]

# # 4. Square root after specific milliseconds
# def sqrt_after_delay(number, ms):
#     time.sleep(ms / 1000.0)
#     result = math.sqrt(number)
#     print(f"Square root of {number} after {ms} milliseconds is {result}")

# # 5. Check if all elements of a tuple are true
# def all_true(t):
#     return all(t)


# # Примеры вызова функций

# # 1. Multiply list
# nums = [1, 2, 3, 4]
# print("Product of list:", multiply_list(nums))  # 24

# # 2. Count cases
# count_case("Hello World!")  # 2 upper, 8 lower

# # 3. Check palindrome
# print("Is palindrome? 'A man, a plan, a canal: Panama':", is_palindrome("A man, a plan, a canal: Panama"))  # True
# print("Is palindrome? 'hello':", is_palindrome("hello"))  # False

# # 4. Square root after delay
# sqrt_after_delay(25100, 2123)

# # 5. Check all true
# print("All true? (True, 1, 'non-empty'):", all_true((True, 1, 'non-empty')))  # True
# print("All true? (True, 0, 'non-empty'):", all_true((True, 0, 'non-empty')))  # False
