# CSP - Subject Timetable using Backtracking

subjects = ["Maths", "Python", "DBMS", "AI"]

time_slots = ["9:00 AM", "11:00 AM", "2:00 PM"]

# Constraints: these pairs cannot have the same time slot
constraints = [
    ("Maths", "Python"),
    ("DBMS", "AI")
]

timetable = {}


def is_valid(subject, slot):
    for s1, s2 in constraints:
        if subject == s1:
            other = s2
        elif subject == s2:
            other = s1
        else:
            continue

        if timetable.get(other) == slot:
            return False

    return True


def backtrack(index):
    if index == len(subjects):
        return True

    subject = subjects[index]

    for slot in time_slots:
        if is_valid(subject, slot):
            timetable[subject] = slot

            if backtrack(index + 1):
                return True

            del timetable[subject]

    return False


# Solve the CSP
if backtrack(0):
    print("Final Timetable:")
    for subject in subjects:
        print(subject, "->", timetable[subject])
else:
    print("No solution found.")