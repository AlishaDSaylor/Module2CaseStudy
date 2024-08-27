# Author: Alisha Saylor
# File Name: case_study_student.py
# Description: This app accepts student names and GPAs and checks if the student qualifies
#              for either the Dean's List or the Honor Roll.

def main():
    while True:
        # Ask for the student's last name. .strip to remove spaces
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ").strip()
        if last_name.upper() == 'ZZZ':
            break  # Exit the loop if the user enters 'ZZZ' and .upper to automatically capitolize the response

        # Ask for the student's first name
        first_name = input("Enter the student's first name: ").strip()

        # Ask for the student's GPA
        try:
            gpa = float(input("Enter the student's GPA: "))
        except ValueError:
            print("Invalid GPA. Please enter a number.")
            continue

        # Check if the student qualifies for the Dean's List or Honor Roll
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} does not qualify for the Dean's List or Honor Roll.")

if __name__ == "__main__":
    main()