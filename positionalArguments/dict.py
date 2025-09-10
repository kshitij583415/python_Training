# positional arguments in dict


def student_info(name, age):
    print(f"{name} is {age} years old")

info = {"name": "Kshitij", "age": 21}

student_info(**info)

# output
# Kshitij is 21 years old