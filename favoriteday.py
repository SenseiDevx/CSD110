from datetime import date

# Get today's day of the month
today = date.today().day

# Display today's date
print(f"Today is the: {today} day of the month")

# Ask the user for their favorite day of the month
favorite_day = int(input("What is your favorite day of the month? "))

# Calculate the difference
if favorite_day == today:
    print("Your favorite day is today!")
elif favorite_day < today:
    days_ago = today - favorite_day
    print(f"Your favorite day was {days_ago} day(s) ago.")
else:
    days_until = favorite_day - today
    print(f"Your favorite day is in {days_until} day(s).")
