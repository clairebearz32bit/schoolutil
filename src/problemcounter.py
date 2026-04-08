from math import floor, ceil
from re import split

"""
:parameter ranges : takes in a list of 3D tuples where index 0 and 1 are the start and stop index, and index 2 is the step.
"""


class Ranges:
    def __init__(self, ranges: list[tuple[int, int, int]], exclude: list[int] = None, *other_ranges: list[object]):
        if exclude is not None:
            self.exclude = exclude

        else:
            self.exclude = []

        self.ranges = ranges

        if not all([0 <= _range[0] <= _range[1] for _range in self.ranges]):
            raise TypeError("_range must be a tuple of integers with 0 <= the start index <= the end index.")
    # set op to True for subtraction
    def add_or_subtract_other_ranges(self, other_ranges: list[object], op=True):
        if not all([isinstance(_other, Ranges) for _other in other_ranges]):
            raise TypeError("other_ranges must all be instances of Ranges().")

        for _other in other_ranges:
            _other = Ranges([], *other_ranges)
            self.exclude += (-op) * _other.exclude
            self.ranges += _other.ranges

    def get_total(self):
        # distance between each range
        total = 0

        for _range in self.ranges:
            dist = _range[1] - _range[0]
            dist = ceil(dist / _range[2])
            dist += 1

            total += dist

        # distances = [ceil((_range[1]-_range[0]) / self.step)+1 for _range in self.ranges]
        # print(distances)

        return total - len(self.exclude)

    def __str__(self):
        return


def parse_ranges(ranges: str):
    ranges = split(r"[\\:\s+]", ranges)

    if len(ranges) % 3 != 0:
        raise Exception("Invalid range format, make sure each range is in the format start_index:end_index:step.")

    get_range = lambda n: [int(i) for i in ranges[n::3]]

    starts = get_range(0)
    ends = get_range(1)
    steps = get_range(2)

    return list(zip(starts, ends, steps))

# TODO Write class to return __str__ of grade
def get_grades(probs_done, probs_total, weight=None):
    percent = probs_done / probs_total

    if weight is not None:
        return (percent / weight) * 100

    return percent


def num_to_letter_grade(grade):
    if grade < 60:
        return "F"

    if grade > 100:
        return IndexError("Grade must be between 0-100.")

    grades = {60: "D", 70: "C", 80: "B", 90: "A"}
    rounded = 10 * floor(grade / 10)

    return grades[rounded]


if __name__ == '__main__':
    ranges = "3:93:2 3:39:2 3:20:1 41:44:1 3:39:2"
    ranges = parse_ranges(ranges)
    probs_total = Ranges(ranges, exclude=[9, 10, 11, 15]).get_total()


    # probs_done = ch1done + ch2done + ch3done
    # probs_total = ch1total + ch2total + ch3total

    # grade_num = get_grades(probs_done, probs_total)
    # grade_letter = num_to_letter_grade(grade_num*100)
    #
    # print(f"Finished: {probs_done}/{probs_total}"
    #       f"\nGrade: {grade_num*100:.2f}% ({grade_letter})"
    #       f"\nPoints: {grade_num*16.67:.0f}/16.67")
