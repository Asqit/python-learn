# List comprehensions
# allows you to transform a list with less code
# syntax:
# > list = [expression for item in iterable]
# > list = [expression for item in iterable if condition]
# > list = [expression if/else for item in iterable]

# Example_1 list of squared numbers
# alternative way to get squared numbers
# > for i in raw:
# >     squared.append(i * i)
raw = list(range(0, 100))
squared = [number**2 for number in raw]


# Example_2 list of even numbers (reusing raw variable)
even_numbers = [number for number in raw if number % 2 == 0]


# Example_3 passed students
# Czech grading system:
# 1 = amazing
# 2 = great
# 3 = good
# 4 = enough
# 5 = failed

results = [1, 3, 2, 5, 4, 5, 5, 3, 3, 2, 1]
evaluated = ["Failed" if number == 5 else number for number in results]


print(evaluated)  # [1, 3, 2, 'Failed', 4, 'Failed', 'Failed', 3, 3, 2, 1]
