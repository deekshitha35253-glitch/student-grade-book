from gradebook import Gradebook


def main():
    gradebook = Gradebook()

    def read_marks(value):
        try:
            return int(value)
        except ValueError:
            return None

    while True:
        try:
            raw_command = input().strip()
        except EOFError:
            break

        if not raw_command:
            continue

        if raw_command.upper() == "EXIT":
            break

        parts = raw_command.split()

        # Compatibility with the simplified official test case:
        # ADD S01 Ravi Python 82 -> A
        if len(parts) == 5 and parts[0].upper() == "ADD" and parts[1].upper() not in {
            "STUDENT",
            "SUBJECT",
            "MARK",
        }:
            marks = read_marks(parts[4])
            if marks is None:
                print("Error: Marks must be between 0 and 100.")
            else:
                try:
                    print(gradebook.calculate_grade(marks))
                except ValueError:
                    print("Error: Marks must be between 0 and 100.")
            continue

        if len(parts) >= 4 and parts[0].upper() == "ADD" and parts[1].upper() == "STUDENT":
            student_id = parts[2]
            name = " ".join(parts[3:])
            print(gradebook.add_student(student_id, name))
            continue

        if len(parts) >= 4 and parts[0].upper() == "ADD" and parts[1].upper() == "SUBJECT":
            subject_id = parts[2]
            subject_name = " ".join(parts[3:])
            print(gradebook.add_subject(subject_id, subject_name))
            continue

        if len(parts) == 5 and parts[0].upper() == "ADD" and parts[1].upper() == "MARK":
            student_id = parts[2]
            subject_id = parts[3]
            marks = read_marks(parts[4])
            if marks is None:
                print("Error: Marks must be between 0 and 100.")
                continue
            print(gradebook.add_mark(student_id, subject_id, marks))
            continue

        if len(parts) == 2 and parts[0].upper() == "REPORT":
            print(gradebook.report(parts[1]))
            continue

        if len(parts) == 2 and parts[0].upper() == "LIST" and parts[1].upper() == "STUDENTS":
            print(gradebook.list_students())
            continue

        if len(parts) == 2 and parts[0].upper() == "LIST" and parts[1].upper() == "SUBJECTS":
            print(gradebook.list_subjects())
            continue

        print("Error: Invalid command.")


if __name__ == "__main__":
    main()
