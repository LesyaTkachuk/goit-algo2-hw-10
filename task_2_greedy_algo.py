# define Teacher class
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()

    def assign_subject(self, subject):
        self.assigned_subjects.add(subject)


# define function for schedule creation using greedy approach
def create_schedule(subjects, teachers):
    schedule = set()

    for subject in subjects:
        teachers_for_subject = []

        for teacher in teachers:
            if subject in teacher.can_teach_subjects:
                teachers_for_subject.append(teacher)

        if len(teachers_for_subject) == 0:
            return None
        elif len(teachers_for_subject) == 1:
            teachers_for_subject[0].assign_subject(subject)
            schedule.add(teachers_for_subject[0])
        else:
            sorted_teachers = sorted(
                teachers_for_subject,
                key=lambda teacher: len(teacher.can_teach_subjects),
                reverse=True,
            )
            max_subjects = len(sorted_teachers[0].can_teach_subjects)
            teachers_with_max_subjects = [
                teacher
                for teacher in sorted_teachers
                if len(teacher.can_teach_subjects) == max_subjects
            ]
            youngest_teacher = min(
                teachers_with_max_subjects, key=lambda teacher: teacher.age
            )
            youngest_teacher.assign_subject(subject)
            schedule.add(youngest_teacher)

    return schedule


if __name__ == "__main__":
    # subjects set
    subjects = {"Math", "Physics", "Chemistry", "Informatics", "Biology"}
    # teachers array
    teachers = [
        Teacher(
            "Oleksandr", "Ivanenko", 45, "o.ivanenko@example.com", {"Math", "Physics"}
        ),
        Teacher("Maria", "Petrenko", 38, "m.petrenko@example.com", {"Chemistry"}),
        Teacher(
            "Sergiy",
            "Kovalenko",
            50,
            "s.kovalenko@example.com",
            {"Math", "Informatics"},
        ),
        Teacher(
            "Nataliia",
            "Shevchenko",
            29,
            "n.shevchenko@example.com",
            {"Biology", "Chemistry"},
        ),
        Teacher(
            "Dmytro",
            "Bondarenko",
            35,
            "d.bondarenko@example.com",
            {"Physics", "Informatics"},
        ),
        Teacher("Olena", "Grytsenko", 42, "o.grytsenko@example.com", {"Biology"}),
    ]

    # create schedule
    schedule = create_schedule(subjects, teachers)

    # Display the results
    if schedule:
        print("Schedule:")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} years, email: {teacher.email}"
            )
            print(f"   Assigned subjects: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Could not create a schedule that cover all subjects.")
