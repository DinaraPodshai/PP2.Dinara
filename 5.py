#Python RegEx (из лекции)

# import re
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)

# findall-Returns a list containing all matches
# search-Returns a Match object if there is a match anywhere in the string
# split-Returns a list where the string has been split at each match
# sub	- Replaces one or many matches with a string

# import re
# #Return a list containing every occurrence of "ai":
# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)

# import re
# txt = "The rain in Spain"
# #Check if "Portugal" is in the string:
# x = re.findall("Portugal", txt)
# print(x)
# if (x):
#   print("Yes, there is at least one match!")
# else:
#   print("No match")


# import re
# txt = "The rain in Spain"
# x = re.search("\s", txt)
# print("The first white-space character is located in position:", x.start()) 


# import re
# txt = "The rain in Spain"
# x = re.search("Portugal", txt)
# print(x)


# import re
# #Split the string at every white-space character:
# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)


# import re
# #Split the string at the first white-space character:
# txt = "The rain in Spain"
# x = re.split("\s", txt, 1)
# print(x)


# import re
# #Replace all white-space characters with the digit "9":
# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt)
# print(x)


# import re
# #Replace the first two occurrences of a white-space character with the digit 9:
# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt, 2)
# print(x)


# import re
# #The search() function returns a Match object:
# txt = "The rain in Spain"
# x = re.search("ai", txt)
# print(x)


# The Match object has properties and methods used to retrieve information about the search, and the result:
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match



# import re
# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.span())


# import re
# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.string)


# import re
# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.group())



#Python RegEx exercises (из regex.md)
# import re

# # 1. Match a string that has an 'a' followed by zero or more 'b's
# def match_a_b_star(s):
#     return re.fullmatch(r'ab*', s)

# # 2. Match a string that has an 'a' followed by two to three 'b's
# def match_a_2_3b(s):
#     return re.fullmatch(r'ab{2,3}', s)

# # 3. Find sequences of lowercase letters joined with an underscore
# def find_lowercase_underscore(s):
#     return re.findall(r'[a-z]+_[a-z]+', s)

# # 4. Find sequences of one uppercase letter followed by lowercase letters
# def find_upper_followed_by_lower(s):
#     return re.findall(r'[A-Z][a-z]+', s)

# # 5. Match a string that has an 'a' followed by anything, ending in 'b'
# def match_a_anything_b(s):
#     return re.fullmatch(r'a.*b', s)

# # 6. Replace all occurrences of space, comma, or dot with a colon
# def replace_space_comma_dot(s):
#     return re.sub(r'[ ,.]', ':', s)

# # 7. Convert snake_case string to camelCase string
# def snake_to_camel(s):
#     return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), s)

# # 8. Split a string at uppercase letters
# def split_at_uppercase(s):
#     return re.split(r'(?=[A-Z])', s)

# # 9. Insert spaces between words starting with capital letters
# def insert_space_before_capital(s):
#     return re.sub(r'(?=[A-Z])', ' ', s).strip()

# # 10. Convert camelCase string to snake_case
# def camel_to_snake(s):
#     return re.sub(r'([A-Z])', r'_\1', s).lower().lstrip('_')


# # Примеры использования
# if __name__ == "__main__":
#     print(match_a_b_star("abbb"))       # <re.Match object> or None
#     print(match_a_2_3b("abb"))          # <re.Match object> or None
#     print(find_lowercase_underscore("this_is_a_test example_string"))  # ['this_is', 'example_string']
#     print(find_upper_followed_by_lower("HelloWorld ExampleTest"))      # ['Hello', 'World', 'Example', 'Test']
#     print(match_a_anything_b("aXYZb"))  # <re.Match object> or None
#     print(replace_space_comma_dot("Hello, world. How are you"))        # 'Hello::world::How:are:you'
#     print(snake_to_camel("this_is_a_test"))                            # 'thisIsATest'
#     print(split_at_uppercase("HelloWorldExample"))                     # ['', 'Hello', 'World', 'Example']
#     print(insert_space_before_capital("HelloWorldExample"))            # 'Hello World Example'
#     print(camel_to_snake("helloWorldExample"))                         # 'hello_world_example'



#Python RegEx exercises- используя row.txt

# 1. Извлечение email-адресов
# import re


# def extract_emails(text):
#     pattern = r'\b[\w.-]+@[\w.-]+\.(?:com|org|net)\b'
#     return re.findall(pattern, text)
# # Пример:
# text = "Contact us at info@example.com, hello.world@site.net or support@domain.org"
# print("Emails found:", extract_emails(text))

# #2
# def extract_ip_timestamp(log_text):
#     pattern = r'(\d{1,3}(?:\.\d{1,3}){3}) \S+ \S+ \[(.*?)\]'
#     return re.findall(pattern, log_text)
# # Пример:
# log = '127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET /index.html HTTP/1.0" 200 2326'
# print("IP and Timestamp:", extract_ip_timestamp(log))

# #3
# def validate_password(pwd):
#     pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
#     return bool(re.fullmatch(pattern, pwd))
# # Примеры:
# print("Password valid:", validate_password("Password1"))  # True
# print("Password valid:", validate_password("password"))   # False


# #4
# def extract_hashtags(tweet):
#     pattern = r'#\w+'
#     return re.findall(pattern, tweet)
# # Пример:
# tweet = "Loving the new #AI and #Python3 update! Check out #ChatGPT"
# print("Hashtags found:", extract_hashtags(tweet))



# #5
# def normalize_phone_number(phone):
#     digits = re.sub(r'\D', '', phone)  # Удалить всё, кроме цифр
#     if digits.startswith('8'):
#         digits = '7' + digits[1:]
#     if len(digits) == 11 and digits.startswith('7'):
#         return f"+7 ({digits[1:4]}) {digits[4:7]}-{digits[7:9]}-{digits[9:11]}"
#     else:
#         return "Некорректный номер"
# # Примеры:
# print("Normalized:", normalize_phone_number('+7 701 123 4567'))
# print("Normalized:", normalize_phone_number('87011234567'))
# print("Normalized:", normalize_phone_number('7-701-123-45-67'))
