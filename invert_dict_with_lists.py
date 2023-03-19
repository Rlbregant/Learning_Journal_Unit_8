# Description: Inverts a dictionary with lists as values
def invert_dict_with_lists(d):
    # Inverting the dictionary
    inverse = dict()
    # For each key in the dictionary
    for key in d:
        # For each value in the list of values
        val = d[key]
        # If the value is not in the inverse dictionary
        for val in val:
            # Add the key to the inverse dictionary
            if val not in inverse:
                # The value is a list with the key
                inverse[val] = [key]
            else:
                inverse[val].append(key)
    return inverse


def main():
    # Input and output files
    input_file = "gear_sets.txt"
    output_file = "inverted_gear_sets.txt"

    # Reading the dictionary from input file
    with open(input_file, "r") as f:
        # The dictionary is stored as a string
        gear_sets = eval(f.read())

    # Inverting the dictionary
    inverted_gear_sets = invert_dict_with_lists(gear_sets)

    # Writing the inverted dictionary to output file
    with open(output_file, "w") as f:
        # The dictionary is stored as a string
        f.write(str(inverted_gear_sets))

    print("Original gear sets:", gear_sets)
    print("")
    print("Inverted gear sets:", inverted_gear_sets)
    print("")
    print("Output file:", output_file)


if __name__ == "__main__":
    main()

# The program starts by defining a function that inverts the dictionary. It creates a new empty dictionary called
# "inverse" and loops over each key in the input dictionary. For each key, it loops over each value in the list of
# values associated with that key. If the value is not already in the "inverse" dictionary, it adds the value as a
# key and sets its value to a list with the original key. If the value is already in the "inverse" dictionary,
# it appends the original key to the list of values associated with that value. The function returns the "inverse"
# dictionary. The "main" function of the program reads the input dictionary from a file, applies the inversion
# function to it, and writes the resulting inverted dictionary to another file. The program opens the input file and
# reads its contents, which are a string representation of the dictionary. The "eval" function is used to convert
# this string back into a dictionary object that the program can work with. The inversion function is then applied to
# this dictionary to create the inverted dictionary. Finally, the program writes the inverted dictionary to a new
# output file using the "write" function. The program then prints the original dictionary, the inverted dictionary,
# and the name of the output file to the console.
