# 1.	Building a small system for a college to process student project details.
# Write a Python program that:
# Step 1 – Case Conversion (upper, lower, title, capitalize)
# Take the student’s full name and the project title as input.
# Display the name and project title in:
# Uppercase (for display boards)
# Lowercase (for email IDs)
# Title case (for certificates)
# Capitalized (for reports).
# Step 2 – Searching & Counting (find, index, count, startswith, endswith)
# Take the project description as input.
# Find the index of the first occurrence of the word "research".
# Count how many times "innovation" appears.
# Check if the description starts with "This project" and ends with "Thank you".
# Step 3 – Modifying (replace, strip, split, join)
# Remove leading and trailing spaces in the description.
# Replace every occurrence of "difficult" with "challenging".
# Split the description into words.
# Join the words with "-" and display it.
# Step 4 – Validation (isdigit, isalpha, isalnum)
# Ask the student to enter a project ID.
# Check if it is alphanumeric (isalnum()).
# If it is only alphabetic (isalpha()), print "Project ID should include numbers."
# If it is only numeric (isdigit()), print "Project ID should include letters."
# Step 5 – Formatting (format, f-string)
#        Finally, display a summary report in two ways:
# Using .format()
# Using an f-string


name = input("Enter your name: ")
projectTitle = input("Enter your project title: ")

print(f"For display board: {name.upper()}, {projectTitle.upper()}")
print(f"For Email id: {name.lower()}, {projectTitle.lower()}")
print(f"For Certificate: {name.title()}, {projectTitle.title()}")
print(f"For Report: {name.capitalize()}, {projectTitle.capitalize()}")


projectDesc = input("Enter your project description: ")
print(f"index of the first occurrence of the word research is {projectDesc.find("research")}")
print(f"innovation appears for {projectDesc.count("innovation")} times")
print(f"Project starts with This Project: {projectDesc.startswith('This Project')} and ends with Project: {projectDesc.endswith('Thankyou')}")

print(projectDesc.strip())
print(projectDesc.replace("difficult", "challenging"))
print(projectDesc)
desc=projectDesc.split(" ")
print(desc)
print("-".join(desc))

projectId = input("Enter your project ID: ")
print(f"Project ID is alphanumeric: {projectId.isalnum()}")
if projectId.isalpha():
    print("Project ID should include numbers")
elif projectId.isdigit():
    print("Project ID should include letters.")

print("Suummary: Name of the student is {}, his project title is {}, and Project ID is {} and its description is {}".format(name, projectTitle, projectId, projectDesc))

print(f"Suummary: Name of the student is {name}, his project title is {projectTitle}, and Project ID is {projectId} and its description is {projectDesc}.")

print("Project desc:%s" % projectDesc)

# output
# Enter your name: kshitij singh
# Enter your project title: brain tumor classification 
# For display board: KSHITIJ SINGH, BRAIN TUMOR CLASSIFICATION 
# For Email id: kshitij singh, brain tumor classification
# For Certificate: Kshitij Singh, Brain Tumor Classification
# For Report: Kshitij singh, Brain tumor classification
# Enter your project description: this will help doctors to classify if tumor is present or not
# index of the first occurrence of the word research is -1
# innovation appears for 0 times
# Project starts with This Project: False and ends with Project: False
# this will help doctors to classify if tumor is present or not
# this will help doctors to classify if tumor is present or not
# this will help doctors to classify if tumor is present or not
# ['this', 'will', 'help', 'doctors', 'to', 'classify', 'if', 'tumor', 'is', 'present', 'or', 'not']
# this-will-help-doctors-to-classify-if-tumor-is-present-or-not
# Enter your project ID: 12j32
# Project ID is alphanumeric: True
# Suummary: Name of the student is kshitij singh, his project title is brain tumor classification , and Project ID is 12j32 and its description is this will help doctors to classify if tumor is present or not
# Suummary: Name of the student is kshitij singh, his project title is brain tumor classification , and Project ID is 12j32 and its description is this will help doctors to classify if tumor is present or not.
# Project desc:this will help doctors to classify if tumor is present or not