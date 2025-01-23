# Ask the user to input a number between 1 and 5
number = int(input("Enter a number between 1 and 5: "))

# Check if the number is outside the valid range
if number < 1 or number > 5:
    print("Error: Please enter a number between 1 and 5.")
else:
    # Dictionary to map numbers to Roman numerals
    roman_numerals = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V"
    }
    # Display the Roman numeral equivalent of the number
    print(f"Roman numeral: {roman_numerals[number]}")
