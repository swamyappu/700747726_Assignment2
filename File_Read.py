# Write a python program to find the wordcount in a file (input.txt) for each line and then print the output.
# Finally store the output in output.txt file.
# C:\Users\Swamy\OneDrive\Desktop
file_loc = input("File Location to read \n")
file_sav = input("File Location to save Output \n")
file_raw = open(file_loc, "r")
file_sav1 = open((file_sav + "\output.txt"), "a")

counter = {}

for j in file_raw:
    file_sav1.write(j)
file_sav1.write("\n")
file_raw = open(file_loc, "r")

for i in file_raw:
    k = i.split()
    c = 0
    for n in k:
        if n in counter:
            counter[n] += 1
        else:
            counter[n] = 1

for i in counter:
    val = i + ":" + str(counter[i])
    file_sav1.write(val + "\n")
    print(val)

file_sav1.close()
file_raw.close()
