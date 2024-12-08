# Function to determine grade point and remark based on marks
def get_grade_point_and_remark(marks):
    if marks >= 90:
        return 10, "OUTSTANDING"
    elif marks >= 80:
        return 9, "VERY GOOD"
    elif marks >= 70:
        return 8, "GOOD"
    elif marks >= 60:
        return 7, "AVERAGE"
    elif marks >= 50:
        return 6, "PASS"
    else:
        return 0, "FAIL"

# Main function to input student details and display them
def main():
    # Taking input from the user
    name = input("Enter Name: ")
    roll_number = input("Enter Roll Number: ")
    marks = float(input("Enter Marks secured for Mathematics Examination (out of 100): "))

    # Getting grade point and remark
    grade_point, remark = get_grade_point_and_remark(marks)

    # Displaying the student details
    print("\nStudent Details:")
    print(f"Name: {name}")
    print(f"Roll Number: {roll_number}")
    print(f"Marks: {marks}")
    print(f"Grade Point: {grade_point}")
    print(f"Remark: {remark}")

# Running the main function
if __name__ == "__main__":
    main()
