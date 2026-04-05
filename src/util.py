from math import floor

def count_problems(start, end, step=2, omitted=None, end_inclusive=True):
    if start >= end:
        raise IndexError("Start problem must be smaller than end problem.")

    omitted = len(omitted) if omitted is not None else 0

    total = len([i for i in range(start, end + end_inclusive, step)]) - omitted

    return total


# TODO Write class to return __str__ of grade
def get_grades(probs_done, probs_total, weight=None):
    percent = probs_done / probs_total

    if weight is not None:
        return (percent / weight) * 100

    return percent * 100


def num_to_letter_grade(grade):
    if grade < 60:
        return "F"

    if grade > 100:
        return IndexError("Grade must be between 0-100.")

    grades = {60: "D", 70: "C", 80: "B", 90: "A"}
    rounded = 10 * floor(grade / 10)

    return grades[rounded]


if __name__ == '__main__':
    probs_done = count_problems(45, 69)
    probs_total = count_problems(7, 69)
    grade_num = get_grades(probs_done, probs_total, weight=16.67)
    grade_letter = num_to_letter_grade(grade_num)

    print(f"Finished: {probs_done}/{probs_total}\nGrade: {grade_num:.2f}% ({grade_letter})")
