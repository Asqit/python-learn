# Lambda functions (anonymous)
# are function which are usually passed as arguments or assigned to a variable for later use
# Usually the syntax is: (params) => return
# or (params) => {}
#
# In python the syntax differs:
# lambda params: expression


def construct_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}"


# js: (first, last) => `${first} ${last}`
construct_name_lambda = lambda first_name, last_name: f"{first_name} {last_name}"

# Both produce the same result, but one is less verbose
print(construct_name("Andrew", "Tuček"))
print(construct_name_lambda("Andrew", "Tuček"))
