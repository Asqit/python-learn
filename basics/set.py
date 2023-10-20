# Set
# another very common data structure is Set.
# set is unordered list of immutable elements.
# Each element is unique and cannot repeat (no duplicates)
# elements cannot be changes

# example of a Set
my_skills = {"Python", "JavaScript", "Typescript", "Java", "BASH"}

# getting size of a set
print(f"my_skills is {len(my_skills)} items long")

# check if element exist in set
if "Python" in my_skills:
    print("Python does exists in my_skills")

# Adding element to a Set
my_skills.add("React.js")

# removing element
my_skills.remove("BASH")

# Freezing the set (making it immutable)
my_skills = frozenset(my_skills)

# This will raise an exception, because the set is frozen
my_skills.add("Django")
