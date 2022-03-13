import itertools
import os

print("Press <enter> to skip.")

first_name = input("Enter target first name: ").strip()
surname = input("Enter target surname: ").strip()
last_name = input("Enter target last name: ").strip()
birthdate = input("Enter target birthday (ddmmyyyy): ").strip()
phone_number = input("Enter phone number: ").strip()
print()
partner_name = input("Enter partner name: ").strip()
partner_nickname = input("Enter partner nickname: ").strip()
partner_birthdate = input("Enter partner date of birth (ddmmyyyy): ").strip()
print()
child_name = input("Enter child name: ")
child_nickname = input("Enter child nickname: ")
child_birthdate = input("Enter child date of birth (ddmmyyyy): ")
print()
pets_name = input("Enter pets name: ")
company_name = input("Enter company name: ")

default_output = os.path.join(os.path.expanduser("~"), "wordlist.txt")
output_path = input(f"Specify output file (default {str(default_output)}): ")
if output_path == "":
    output_path = default_output

combination_list = [
    first_name,
    surname,
    last_name,
    phone_number,
    birthdate,
    partner_name,
    partner_nickname,
    partner_birthdate,
    child_name,
    child_nickname,
    child_birthdate,
    pets_name,
    company_name,
]

combination_list = list(filter(None, combination_list))

# make combination_list combination lowercase and remvoe whitespace
combination_list = list(map(lambda x: x.lower(), combination_list))
combination_list = list(map(lambda x: x.replace(" ", ""), combination_list))


# Loading
print("\n\nPlease wait...\n\n")

wordlist = []

# Append combination of all upper and lower case letters of combination_list
processed_combination_list = []
for combination in combination_list:
    if str(combination).isnumeric():
        continue

    list_text_combination = list(
        map("".join, itertools.product(*zip(combination.upper(), combination.lower())))
    )
    list_text_combination.remove(combination)
    processed_combination_list.extend(list_text_combination)


for index_1, combination in enumerate(combination_list):
    for index_2, another_combination in enumerate(combination_list):

        # When the combination is same, then skip it
        if index_1 == index_2:
            continue

        # When it's all alphabetic, then make combination for each letter
        wordlist.append(combination + "_" + another_combination)
        wordlist.append(combination + another_combination)
        wordlist.append(combination + "-" + another_combination)

with open(output_path, "w") as file:
    for word in set(wordlist):
        file.write(word + "\n")

print("Wordlist successfully generated!\n")
print(f"Total wordlist: {len(wordlist)}")
print(f"Output file: {output_path}")
