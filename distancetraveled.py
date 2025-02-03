# User data entry
speed = int(input("Enter the speed of the vehicle (in mph): "))
hours = int(input("Enter the number of hours traveled: "))

# Title of table
print("Hour\tDistance Traveled")
print("---------------------------")

# Loop for calculating and outputting distance
for hour in range(1, hours + 1):
    distance = speed * hour
    print(f"{hour}\t{distance}")
