def create_new_string(input_string):
    if len(input_string) < 2:
        return ""
    return input_string[:2] + input_string[-2:]


user_input = input("Enter a string: ")

result = create_new_string(user_input)

print("New string:", result)