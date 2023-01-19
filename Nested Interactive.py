# Write a program, which reads heights (inches.) customers into a list and convert these heights to
# centimeters in a separate list using: 1) Nested Interactive loop. 2) List comprehensions

inc = []
i = 1
b = input("Enter Height " + str(i) + "\n")
inc.append(b)
while b != "":
    i = i + 1
    b = input("Enter Height " + str(i) + "\n")  # Interactive Loop
    if b != "":
        inc.append(b)
    else:
        cm = [(int(i) * 2.54) for i in inc]     # List Comprehension
        print(cm)
