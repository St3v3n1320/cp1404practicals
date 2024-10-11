FILENAME = "subject_data.txt"


def main():
    subjects = get_subjects()
    display_subjects(subjects)


def get_subjects():
    subjects = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            subjects.append(parts)
    return subjects


def display_subjects(subjects):
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students.")


main()