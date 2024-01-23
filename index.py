def check_eligibility(age, communication_skills, marks_percentage, has_government_id):
    if age >= 18 and communication_skills and marks_percentage >= 60 and has_government_id:
        return True
    else:
        return False

def main():
    try:
        age = int(input("Enter your age: "))
        communication_skills = input("Do you have good communication skills? (yes/no): ").lower() == 'yes'
        marks_percentage = float(input("Enter your marks percentage: "))
        has_government_id = input("Do you have a government ID proof? (yes/no): ").lower() == 'yes'

        if check_eligibility(age, communication_skills, marks_percentage, has_government_id):
            print("Congratulations! You are eligible for the job.")
            print("Please note: The job comes with a 2-year bond.")
        else:
            print("Sorry, you do not meet the eligibility criteria for the job.")
    except ValueError:
        print("Invalid input. Please enter valid information.")

if _name_ == "_main_":
    main()
