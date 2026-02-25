# Stage 3: Student Grade Calculator

# Taking input
name = input("Enter student name: ")

mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

# Validate marks
if (mark1 < 0 or mark1 > 100 or
        mark2 < 0 or mark2 > 100 or
        mark3 < 0 or mark3 > 100):

    print("Marks should be between 0 and 100.")

else:
    # Calculations
    total = mark1 + mark2 + mark3
    percentage = (total / 300) * 100

    # Grade logic
    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "F"

    # Output
    print("\nStudent Name:", name)
    print("Total:", total, "/300")
    print("Percentage:", percentage, "%")
    print("Grade:", grade)