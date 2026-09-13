# ---------------- STUDENT MANAGEMENT SYSTEM ----------------


# ---------------- PARENT CLASS ----------------

class Student:

    def __init__(self, roll_no, name, age, course, marks):

        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks


    # ---------------- DISPLAY DETAILS ----------------

    def display_details(self):

        print("\n------ STUDENT DETAILS ------")

        print("Roll No :", self.roll_no)
        print("Name    :", self.name)
        print("Age     :", self.age)
        print("Course  :", self.course)
        print("Marks   :", self.marks)


    # ---------------- CHECK RESULT ----------------

    def check_result(self):

        if self.marks >= 40:
            print("Result  : PASS")
        else:
            print("Result  : FAIL")


# ---------------- CHILD CLASS ----------------

class CollegeStudent(Student):

    def __init__(self, roll_no, name, age, course, marks):

        super().__init__(roll_no, name, age, course, marks)


    # ---------------- STUDENT TYPE ----------------

    def show_student_type(self):

        print("Student Type: College Student")


# ---------------- STUDENT MANAGEMENT CLASS ----------------

class StudentManagement:

    def __init__(self):

        self.students = {}


    # ---------------- ADD STUDENT ----------------

    def add_student(self, roll_no, name, age, course, marks):

        if roll_no in self.students:

            print("Roll number already exists")

        else:

            student = CollegeStudent(
                roll_no,
                name,
                age,
                course,
                marks
            )

            self.students[roll_no] = student

            print("Student added successfully")


    # ---------------- SEARCH STUDENT ----------------

    def search_student(self, roll_no):

        if roll_no in self.students:

            student = self.students[roll_no]

            print("\nStudent Found")

            student.display_details()
            student.check_result()

            return student

        else:

            print("Student not found")

            return None


    # ---------------- DELETE STUDENT ----------------

    def delete_student(self, roll_no):

        if roll_no in self.students:

            del self.students[roll_no]

            print("Student deleted successfully")

        else:

            print("Student not found")


# ---------------- CREATE STUDENT MANAGEMENT OBJECT ----------------

system = StudentManagement()


# ---------------- MAIN MENU ----------------

while True:

    print("\n------ PYTHON STUDENT MANAGEMENT ------")

    print("1. Add Student")
    print("2. Search Student")
    print("3. View Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")


    # ---------------- ADD STUDENT ----------------

    if choice == "1":

        roll_no = input("Enter Roll Number: ")

        name = input("Enter Name: ")

        age = int(input("Enter Age: "))

        course = input("Enter Course: ")

        marks = float(input("Enter Marks: "))

        system.add_student(
            roll_no,
            name,
            age,
            course,
            marks
        )


    # ---------------- SEARCH STUDENT ----------------

    elif choice == "2":

        roll_no = input("Enter Roll Number: ")

        student = system.search_student(roll_no)


    # ---------------- VIEW STUDENT ----------------

    elif choice == "3":

        roll_no = input("Enter Roll Number: ")

        student = system.search_student(roll_no)

        if student is not None:

            student.show_student_type()


    # ---------------- DELETE STUDENT ----------------

    elif choice == "4":

        roll_no = input("Enter Roll Number: ")

        system.delete_student(roll_no)


    # ---------------- EXIT ----------------

    elif choice == "5":

        print("\nThank you for using Python Student Management System")

        break


    # ---------------- INVALID CHOICE ----------------

    else:

        print("Invalid choice")

