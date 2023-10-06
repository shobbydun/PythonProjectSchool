#sct211-0031/2021
#KITAVI DUNCAN GITAU

#QUESTION 1
from datetime import datetime

#input from the user

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

#current time
current_date = datetime.now()

#claculate the age
birth_date = datetime(birth_year,birth_month,birth_day)
age = current_date - birth_date

#getting years and days from the difference
years = age.days // 365  #divide number of days by 365
days_rem = age.days % 365  #remainder days
months = days_rem // 30    #remainder days divide by 30 to get months
days = days_rem % 30       #remaining days

#display
print(f"Your age is {years} years, {months} months, and {days} days.")


#QUSTION2 

#user input
total_bill = float(input("Enter total Bill Amount: "))
number_of_people = int(input("Enter number of people splitting the bill: "))
tip_percentage = int(input("Enter tip percentage you eish either 10,12,or 15: "))

#check the inputs
if tip_percentage not in [10,12,15] or total_bill <= 0 or number_of_people <=0:
    print("Invalid inputs enter valid one")

else:
    #calculate tip amount
    tip_amount = (total_bill * tip_percentage)/ 100

    #calculate total amount with tip
    total_amount = total_bill + tip_amount

    #calculate amount per person
    amount_per_person = total_amount/number_of_people

    #display result
    print(f"Each person pays: {amount_per_person:.2f}")



#Question 3

#user input
your_weight = float(input("Enter Your weight in Kilograms: "))
your_height = float(input("Enter Your height in metres: "))

#calculate BMI
BMI = your_weight / (your_height*your_height)

#determine whether underweight,over or normal
if BMI < 18.5:
    category = "Underweight"
elif 18.5 <= BMI < 24.9:
    category = "Normal Weight"
else:
    category = "OverWeight"

#display the BMI
print(f"Your BMI is: {BMI:.2f}")
print(f"You are categorized as: {category}")



#Question 4

#get input
year = int(input("Enter a year: "))

#check if its a leap year
if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year")


