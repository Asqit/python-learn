# type casting - converts the data type of a value to another data type
sample_int = -2
sample_str = "42"
sample_float = 3.1459
sample_boolean = False

# Basic
print("raw data types....")
print(type(sample_int))
print(type(sample_str))
print(type(sample_float))
print()


# converting string to multiple different types
print("str to multiple...")
print(int(sample_str))          # integer: 42
print(float(sample_str))        # float: 42.0
print(bool(sample_str))         # boolean: True
print()


# converting float to multiple data types
print("float to multiple...")
print(int(sample_float))        # int: 3
print(str(sample_float))        # str: "3.1459"
print(bool(sample_float))       # boolean: True
print()


# converting int to multiple data types 
print("int to multiple...")
print(str(sample_int))          # str: "2"
print(float(sample_int))        # float: -2.0
print(bool(sample_int))         # boolean: True
print()


# converting bool to multiple data types
print("bool to multiple...")
print(str(sample_boolean))      # str: "False"
print(float(sample_boolean))    # float: 0.0
print(int(sample_boolean))      # int: 0
print()
