# Write a program that takes two strings from the user: first_name, last_name. Pass these variables to
# fullname function that should return the (full name).

first_name = input("enter First Name \n")
last_name = input("enter Last Name \n")


def full_name(fname_arg, lname_arg):
    f_name = fname_arg + " " + lname_arg
    return f_name


print("Full Name is " + full_name(first_name, last_name))
