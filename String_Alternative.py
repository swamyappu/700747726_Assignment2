# Write function named “string_alternative” that returns every other char in the full_name string

strs = input("Enter a string \n")


def string_alternative(alt_stst):
    val = alt_stst[::2]
    return val


def main(stst1):
    fin = string_alternative(stst1)
    return fin


final_Str = main(strs)

print(main(strs))
