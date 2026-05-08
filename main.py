import pandas as pd


def read_data():
    data = pd.read_csv("students.csv")

    print("Student Dataset")
    print(data)

    return data


def average_score(data):
    avg = data["Score"].mean()

    print("\nAverage Score:", round(avg, 2))


def top_students(data):
    top = data[data["Score"] >= 8]

    print("\nTop Students:")
    print(top)


def student_count(data):
    total = len(data)

    print("\nTotal Students:", total)


def main():
    data = read_data()

    average_score(data)

    top_students(data)

    student_count(data)


if __name__ == "__main__":
    main()