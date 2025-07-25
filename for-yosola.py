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

# Question 3.1:
for i in range(1, 11):
    for j in range(1, 11):
        n = i*j
        print(" "*(3-len(str(n))), n, end=" |")
    print()

# Question 3.2:
print("Input the required details to calculate the S.I.")
principal = int(input("Principal amount: "))
duration  = int(input("Time period (years): "))
interest_rate = int(input("Interest rate per annum: "))
if 1 <= principal <= 20 and duration == 2 and interest_rate == 5:
    print("The simple interest is", (principal*duration*interest_rate)/100)
else:
    print("One of your inputs doesn't meet the requirements to perform the S.I operation.")

# Question 3.3:
scores = [13, 57, 55, 100, 17, 38, 7, 16, 37, 17, 100, 63, 66, 36, 49, 19, 79, 10, 7, 83, 80,
          84, 20, 76, 8, 82, 76, 93, 12, 42, 36, 56, 51, 68, 74, 84, 82, 77, 29, 84, 32, 40, 78, 85, 73]
grades = []
for score in scores:
    if 70 <= score <= 100:
        grades.append("A")
    elif 60 <= score <= 69:
        grades.append("B")
    elif 50 <= score <= 59:
        grades.append("C")
    elif  45<= score <= 49:
        grades.append("D")
    elif 40 <= score <= 44:
        grades.append("E")
    elif 0 <= score <= 39:
        grades.append("F")
print(scores, "\n", grades, sep="")

# Question 3.4
# Note compute the value of what in x? i'd just compute x's value.
a = int(input("Input the value of a: "))
b = int(input("Input the value of b: "))
c = int(input("Input the value of c: "))
discriminant = b**2 - 4*a*c
positive_part = (-b + discriminant**0.5) / (2*a)
negative_part = (-b - discriminant**0.5) / (2*a)
if isinstance(positive_part, complex) or isinstance(negative_part, complex):
    x = (positive_part, negative_part)
else:
    x = (round(positive_part, 2), round(negative_part, 2))
print("The values of x are", x[0], "and", x[1])

# Question 3.5:
numbers = [i for i in range(1, 201) if i % 2 == 0]
print(numbers)
average = sum(numbers)/len(numbers)
print("Average is:", average)

# Question 3.6:
num_of_items = int(input("How many items do you want to buy? "))
if num_of_items < 10:
    cost = 12
elif 10 <= num_of_items  <= 99:
    cost = 10
else:
    cost = 7
print("The total cost is:", num_of_items*cost, "NGN")

# Question 3.7:
the_list = [int("1"*num) for num in range(1, 101)]
print(the_list)