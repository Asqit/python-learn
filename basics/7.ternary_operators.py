# Ternary operators or sometimes called "ninja-style" is way to write a condition
# in singular line as expression
# --------------------------------------
# In most language it looks like this:  (condition) ? true : false
# e.g. isEven = 3 % 2 == 0 ? true : false

age = input("Enter your age")

if int(age) >= 18:
    ticket_price = 20
else:
    ticket_price = 5

# the previous code can be simplified using ternary operators:
# syntax: "value_if_true" if condition else "value_if_false"
final_price = 20 if int(age) >= 18 else 5

# Result will be the same
print(ticket_price)
print(final_price)
