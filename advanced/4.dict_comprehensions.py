# Dictionary Comprehensions
# just like list comprehensions, but with dictionaries
# allows you to transform a dict into new one with less code
# Syntax:
# > dict = {key: expression for (key, value) in iterable}
# > dict = {key: expression for (key, value) in iterable if condition}
# > dict = {key: (if/else) for (key, value) in iterable }
# > dict = {key: function(value) for (key, value) in iterable}


greetings = {
    "czech": "Dobrý den",
    "german": "Guten Tag",
    "english": "Good day",
    "polish": "Dzien Dobry",
}

# Example_1 copy
copy_greetings = {key: value for (key, value) in greetings.items()}

# Example_2 only germanic languages
only_german = {key: value for (key, value) in greetings.items() if key == "german"}


# Example_3 hide germanic languages
show_only_slavic = {
    key: (value if key == "polish" or key == "czech" else "non-slavic")
    for (key, value) in greetings.items()
}


# Example_4 transform to non-formal with function
def to_non_format(key: str):
    languages = {
        "czech": "Ahoj",
        "polish": "Cześć",  # čest
        "german": "Hallo",
        "english": "Hello",
    }

    return languages.get(key)


# notice, that we are also omitting the value, but that is optional
non_formals = {key: to_non_format(key) for (key) in greetings.keys()}

print(non_formals)
