class RegistrationSystem:
    def __init__(self):
        self.classes = {}
        self.students = {}

    def create_class(self, class_name, max_size):
        if class_name in self.classes:
            print("Class already exists.")
        else:
            self.classes[class_name] = {'max_size': max_size, 'roster': []}
            print(f"Class '{class_name}' created with a maximum size of {max_size}.")

    def delete_class(self, class_name):
        if class_name in self.classes:
            del self.classes[class_name]
            print(f"Class '{class_name}' deleted.")
        else:
            print("Class does not exist.")

    def enroll_student(self, student_name, class_name):
        if student_name in self.students:
            if class_name in self.classes:
                class_info = self.classes[class_name]
                if len(class_info['roster']) < class_info['max_size']:
                    class_info['roster'].append(student_name)
                    print(f"Student '{student_name}' enrolled in class '{class_name}'.")
                else:
                    print("Class is full. Cannot enroll student.")
            else:
                print("Class does not exist.")
        else:
            print("Student does not exist.")

    def unenroll_student(self, student_name, class_name):
        if student_name in self.students:
            if class_name in self.classes:
                class_info = self.classes[class_name]
                if student_name in class_info['roster']:
                    class_info['roster'].remove(student_name)
                    print(f"Student '{student_name}' unenrolled from class '{class_name}'.")
                else:
                    print(f"Student '{student_name}' is not enrolled in class '{class_name}'.")
            else:
                print("Class does not exist.")
        else:
            print("Student does not exist.")

    def print_student_schedule(self, student_name):
        if student_name in self.students:
            print(f"Class schedule for student '{student_name}':")
            for class_name in self.classes:
                if student_name in self.classes[class_name]['roster']:
                    print(f"- {class_name}")
        else:
            print("Student does not exist.")

    def print_class_roster(self, class_name):
        if class_name in self.classes:
            print(f"Roster for class '{class_name}':")
            for student_name in self.classes[class_name]['roster']:
                print(f"- {student_name}")
        else:
            print("Class does not exist.")

    def print_all_classes(self):
        print("Available classes:")
        for class_name in self.classes:
            print(f"- {class_name}")

    def switch_mode(self):
        mode = input("Enter mode (administrator or student): ").lower()
        if mode == "administrator":
            self.administrator_mode()
        elif mode == "student":
            self.student_mode()
        else:
            print("Invalid mode. Exiting...")

    def administrator_mode(self):
        while True:
            print("\n-- Administrator Mode --")
            print("1. Create a class")
            print("2. Delete a class")
            print("3. Print class roster")
            print("4. Print all classes")
            print("5. Switch mode (Student Mode)")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                class_name = input("Enter the class name: ")
                max_size = int(input("Enter the maximum class size: "))
                self.create_class(class_name, max_size)
            elif choice == "2":
                class_name = input("Enter the class name to delete: ")
                self.delete_class(class_name)
            elif choice == "3":
                class_name = input("Enter the class name to print the roster: ")
                self.print_class_roster(class_name)
            elif choice == "4":
                self.print_all_classes()
            elif choice == "5":
                self.switch_mode()
                break
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def student_mode(self):
        student_name = input("Enter student name: ")
        if student_name not in self.students:
            self.students[student_name] = []
        while True:
            print("\n-- Student Mode --")
            print("1. Enroll in a class")
            print("2. Unenroll from a class")
            print("3. Print class schedule")
            print("4. Switch mode (Administrator Mode)")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                class_name = input("Enter the class name to enroll: ")
                self.enroll_student(student_name, class_name)
            elif choice == "2":
                class_name = input("Enter the class name to unenroll: ")
                self.unenroll_student(student_name, class_name)
            elif choice == "3":
                self.print_student_schedule(student_name)
            elif choice == "4":
                self.switch_mode()
                break
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


registration_system = RegistrationSystem()
registration_system.switch_mode()
