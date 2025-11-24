def above_mean_students(marks):
    """
    Given a dictionary of student marks,
    this function computes the mean and returns
    a list of students whose marks are above the mean.
    """
    # Compute the mean
    values = list(marks.values())
    mean_value = sum(values) / len(values)

    # Find students above the mean
    above_mean = [name for name, mark in marks.items() if mark > mean_value]

    return mean_value, above_mean


# Example usage
students = {'Sam': 80, 'Lia': 55, 'Omar': 70, 'Ria': 95}
mean_value, above_mean_list = above_mean_students(students)

print("Mean:", mean_value)
print("Students above mean:", above_mean_list)
