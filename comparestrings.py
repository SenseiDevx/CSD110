# Program for comparing strings
def compare_strings():
    first_string = input("Enter the first string --> ")
    second_string = input("Enter the second string --> ")

    # Compare strings and output results
    if first_string > second_string:
        print(f"{first_string} > {second_string}")
    elif first_string < second_string:
        print(f"{first_string} < {second_string}")
    else:
        print(f"{first_string} == {second_string}")

    # Pause before program termination
    input("Press any key to continue . . .")

# Start program
if __name__ == "__main__":
    compare_strings()
