import csv
def create_grades_csv():
    data = [
        ["Name", "Subject", "Grade"],
        ["Alice", "Math", "85"],
        ["Bob", "Science", "78"],
        ["Carol", "Math", "92"],
        ["Dave", "History", "74"]
    ]
    with open("grades.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print("grades.csv created successfully!")
def process():
    grades = []
    with open("grades.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["Grade"] = float(row["Grade"])
            grades.append(row)
    subject_total = {}
    subject_count = {}
    for entry in grades:
        subject = entry["Subject"]
        grade = entry["Grade"]
        if subject not in subject_total:
            subject_total[subject] = 0.0
        if subject not in subject_count:
            subject_count[subject] = 0
        subject_total[subject] += grade
        subject_count[subject] += 1
    subject_average = {}
    for subject in subject_average:
        subject_average[subject] = subject_total[subject]/subject_count[subject]
    with open("average_grades.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Subject", "Average grade"])
        for subject, avg in subject_average.items():
            writer.writerow(subject, avg)
    
    print("\nGrades data loaded:")
    for entry in grades:
        print(entry)
    print("\nAverage grades per subject:")
    for subject, avg in subject_average.items():
        print(f"{subject}: {avg}")
    print("\naverage_grades.csv created successfully!")


if __name__ == "__main__":
    create_grades_csv() 
    process()