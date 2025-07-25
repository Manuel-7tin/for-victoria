# Note: Replace "Eren Yeager" with your name everytime it appears.

# Question 1.1:
# Option 1:
print("Eren Yeager\n"*100)
# Option 2: Replace "Eren Yeager" with your name.
for i in range(100):
    print("Eren Yeager")

# Question 1.2:
for i in range(50):
    print("Eren Yeager "*50)
for j in range(50):
    for k in range(50):
        print("Eren Yeager ", end="")
    print()

# Question 1.3:
for i in range(1, 101):
    print(f"{i}\t Eren Yeager")

# Question 1.4:
print((512-282) / (47.48+5))

# Question 1.5:
number = int(input("Enter a number: "))
print("The square of", number, "is", number**2, ".", sep=" ")

# Question 1.6:
num_2 = int(input("Enter a number: "))
print(num_2, 2*num_2, 3*num_2, 4*num_2, 5*num_2, sep="---")

# Question 1.7:
kg = int(input("Insert a weight(kg): "))
print("Weight in pounds is", 2.2 * kg)

"""--------------------------___________________---------------------------"""

# Question 2.1
length = int(input("Enter length in cm: "))
if length < 0:
    print("Your entry is invalid. Please enter a positive number.")
else:
    print("Length in inches is", round(length / 2.54, 2))

# Question 2.2:
# Note: The conversion formula given in the textbook is incorrect.
# Note: I will use it anyway as it is best to follow instructions even if they do not make sense, at least in this case.
# Note: Regardless i will put the correct formula as in inline comment, incase you prefer that.

temp = int(input("Type in a temperature: "))
unit = input("What unit is the temperature in? Celsius or Fahrenheit: ")
if unit.lower() == "celsius":
    print("Temperature in Fahrenheit is", 5 * temp + 32) # Correct formula: 1.8*temp + 32
elif unit.lower() == "fahrenheit":
    print("Temperature in Celsius is", 59 * (temp - 32)) # Correct formula: (temp - 32)/1.8
else:
    print("That is not a temperature unit recognized by this program.")

# Question 2.3:
temp_in_celsius = float(input("Please enter a temperature in celsius: "))
if temp_in_celsius < -273.15:
    print("This temperature is invalid as it is below absolute zero.")
elif temp_in_celsius == -273.15:
    print("This temperature is absolute zero.")
elif -273.15 <= temp_in_celsius < 0:
    print("The temperature is below freezing.")
elif temp_in_celsius == 0:
    print("The temperature is at freezing point.")
elif 0 < temp_in_celsius < 100:
    print("The temperature is in the normal range.")
elif temp_in_celsius == 100:
    print("The temperature is at the boiling point of water.")
elif temp_in_celsius > 100:
    print("The temperature is above the boiling point.")
