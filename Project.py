import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class SchoolManagementSystem:
    def __init__(self):
        try:
            self.students_data = pd.read_csv("students.csv")
            self.library_data = pd.read_csv("library.csv")
        except Exception as e:
            print("Error occurred while saving data:", e)

    def save_data_to_csv(self):
        self.students_data.to_csv("students.csv", index=False)
        self.library_data.to_csv("library.csv", index=False)

    def add_student(self):
        name = input("Enter student name: ")
        roll_no = int(input("Enter student roll number: "))
        new_student = pd.DataFrame({"Name": [name], "Roll No": [roll_no], "Attendance": [0], "Grades": [np.nan]})
        self.students_data = pd.concat([self.students_data, new_student], ignore_index=True)
        print(f"Student '{name}' added successfully.")
        self.save_data_to_csv()

    def mark_attendance(self):
        roll_no = int(input("Enter student roll number: "))
        attendance = float(input("Enter attendance percentage: "))
        self.students_data.loc[self.students_data['Roll No'] == roll_no, 'Attendance'] = attendance
        print(f"Attendance marked for Roll No '{roll_no}'.")
        self.save_data_to_csv()

    def record_subject_scores(self):
        roll_no = int(input("Enter student roll number: "))
        physics = float(input("Enter Physics score: "))
        chemistry = float(input("Enter Chemistry score: "))
        maths = float(input("Enter Maths score: "))
        ip = float(input("Enter IP score: "))
        pe = float(input("Enter Physical Education score: "))
        
        self.students_data.loc[self.students_data['Roll No'] == roll_no, 'Physics'] = physics
        self.students_data.loc[self.students_data['Roll No'] == roll_no, 'Chemistry'] = chemistry
        self.students_data.loc[self.students_data['Roll No'] == roll_no, 'Maths'] = maths
        self.students_data.loc[self.students_data['Roll No'] == roll_no, 'IP'] = ip
        self.students_data.loc[self.students_data['Roll No'] == roll_no, 'Physical Education'] = pe
        
        print(f"Subject scores recorded for Roll No '{roll_no}'.")
        self.save_data_to_csv()

    def plot_attendance_chart(self):
        plt.bar(self.students_data["Name"], self.students_data["Attendance"])
        plt.xlabel("Students")
        plt.ylabel("Attendance Percentage")
        plt.title("Student Attendance")

        # Annotate each bar with its attendance percentage
        for i, attendance in enumerate(self.students_data["Attendance"]):
            plt.text(i, attendance, f"{attendance:.1f}%", ha='center', va='bottom')

        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def display_students(self):
        print(self.students_data)

    def view_student_details(self):
        search_term = input("Enter student name or roll number to search: ")
        # Convert the 'Roll No' column to strings
        self.students_data['Roll No'] = self.students_data['Roll No'].astype(str)
        student_info = self.students_data[
            (self.students_data['Name'].str.contains(search_term, case=False)) |
            (self.students_data['Roll No'].str.contains(search_term, case=False))
        ]
        print(student_info)
        
    def update_student_records(self):
        print(self.students_data)
        roll_no = int(input("Enter student roll number to update: "))  # Convert to int
        student_info = self.students_data[self.students_data['Roll No'] == roll_no]

        if not student_info.empty:
            print("Current Student Details:")
            print(student_info)

            field = input("Enter the field to update (Name/Attendance/Grades): ")
            value = input("Enter the new value: ")
            self.students_data.loc[self.students_data['Roll No'] == roll_no, field] = value
            print(f"Record updated for Roll No '{roll_no}'.")
            self.save_data_to_csv()
        else:
            print(f"Student with Roll No '{roll_no}' not found.")

    def delete_student_record(self):
        roll_no = int(input("Enter student roll number to delete: "))
        self.students_data = self.students_data[self.students_data['Roll No'] != roll_no]
        print(f"Student with Roll No '{roll_no}' deleted.")
        self.save_data_to_csv()

    def calculate_average_attendance(self):
        average_attendance = self.students_data["Attendance"].mean()
        print(f"Average Attendance: {average_attendance:.2f}%")

    def calculate_average_grades(self):
        subjects = ['Physics', 'Chemistry', 'Maths', 'IP', 'Physical Education']

        for subject in subjects:
            self.students_data[subject] = pd.to_numeric(self.students_data[subject], errors='coerce')

        self.students_data['Average_Grades'] = self.students_data[subjects].mean(axis=1)
        self.students_data['Average_Grades'] = self.students_data['Average_Grades'].apply(lambda x: f"{x:.2f}" if not pd.isna(x) else "")

        print(self.students_data)

    def view_library_books(self):
        print("\nLibrary Books:")
        print(self.library_data)

    def issue_book(self):
        print("\nLibrary Books:")
        print(self.library_data)
        book = input("Enter book name: ")
        student = input("Enter student name: ")
        issue_date = input("Enter issue date (YYYY-MM-DD): ")
        new_issue = pd.DataFrame({"Book": [book], "Student": [student], "Issue Date": [issue_date]})
        self.library_data = pd.concat([self.library_data, new_issue], ignore_index=True)
        print(f"Book '{book}' issued to student '{student}' on {issue_date}.")
        self.save_data_to_csv()

    def return_book(self):
        print("\nLibrary Books:")
        print(self.library_data)
        book = input("Enter book name: ")
        student = input("Enter student name: ")
        return_date = input("Enter return date (YYYY-MM-DD): ")
        # Check if the book is issued to the specified student
        if any((self.library_data["Book"] == book) & (self.library_data["Student"] == student)):
            self.library_data = self.library_data[
                ~((self.library_data["Book"] == book) & (self.library_data["Student"] == student))
            ]
            print(f"Book '{book}' returned by student '{student}' on {return_date}.")
            self.save_data_to_csv()
        else:
            print(f"Book '{book}' is not issued to student '{student}'.")

def main():
    print("Welcome to School Management System")
    school = SchoolManagementSystem()

    while True:
        print("\nMenu:"
"\n1. Add Student"
"\n2. Mark Attendance"
"\n3. Record Subject Scores"
"\n4. Plot Attendance Chart"
"\n5. Display Students"
"\n6. View Student Details"
"\n7. Update Student Records"
"\n8. Delete Student Record"
"\n9. Calculate Average Attendance"
"\n10. Calculate Average Grades"
"\n11. View Library Books"
"\n12. Issue Book"
"\n13. Return"
"\n14. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10/11/12/13/14): ")

        if choice == "1":
            school.add_student()
        elif choice == "2":
            school.mark_attendance()
        elif choice == "3":
            school.record_subject_scores()
        elif choice == "4":
            school.plot_attendance_chart()
        elif choice == "5":
            school.display_students()
        elif choice == "6":
            school.view_student_details()
        elif choice == "7":
            school.update_student_records()
        elif choice == "8":
            school.delete_student_record()
        elif choice == "9":
            school.calculate_average_attendance()
        elif choice == "10":
            school.calculate_average_grades()
        elif choice == "11":
            school.view_library_books()
        elif choice == "12":
            school.issue_book()
        elif choice == "13":
            school.return_book()
        elif choice == "14":
            school.save_data_to_csv()
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()