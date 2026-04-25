marks1 = int(input("Enter the marks of the first subject: "))
marks2 = int(input("Enter the marks of the second subject: "))
marks3 = int(input("Enter the marks of the third subject: "))
dict = {}
dict.update({"Python": marks1})
dict.update({"java": marks2})
dict.update({"AI": marks3})
print("The subjects and their marks are: ", dict)
