# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: GPA Calculator
# Shengnan Zhou
# Last Modified: June 12, 2018
# ---------------------------------------
# Calculate GPA for students
# with their inputs of number of
# courses, grades, and credits.
# ---------------------------------------





def main():

    number = int(input("Enter the number of courses you are taking: "))
    while number >= 8 or number <= 0:
        print("The number you entered was invalid. Must be between 1 and 7.")
        number = int(input("Enter the number of courses you are taking: "))
    print()

    top = 0
    bottom = 0

    for i in range(1, number + 1):
        value = translate(i)

        credit = int(input("Enter the credits for course " + str(i) + " : "))
        while credit <= 0 or credit >= 6:
            print("The number you entered was invalid. Must be between 1 and 5.")
            credit = int(input("Enter the credits for course " + str(i) + " : "))

        top = top + value * credit
        bottom = bottom + credit
        print()


    GPA = top / bottom
    GPA = format(GPA, ".2f")
    print("Your GPA is", GPA)





def translate(x):
    grade = str(input("Enter the grade for course " + str(x) +  " : "))
    grade = grade.upper()

    if grade == "A":
        value = 4.0
    elif grade == "A-":
        value = 3.7
    elif grade == "B+":
        value = 3.3
    elif grade == "B":
        value = 3.0
    elif grade == "B-":
        value = 2.7
    elif grade == "C+":
        value = 2.3
    elif grade == "C":
        value = 2.0
    elif grade == "C-":
        value = 1.7
    elif grade == "D+":
        value = 1.3
    elif grade == "D":
        value = 1.0
    elif grade == "F":
        value = 0.0
    return value




main()
