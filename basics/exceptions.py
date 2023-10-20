# Exception
# an event detected during runtime that interrupts the flow of a program (Error)


try:
    x = int(input("Enter a number to divide: "))
    y = int(input("Enter a number to divide by: "))
    result = x / y
except ZeroDivisionError:
    print("Cannot divide by 0")
except ValueError:
    print("only numbers are considered valid type")
except Exception as e:
    print(f"something went wrong: {e}")
else:
    # only print result if there are no exceptions
    print(result)
finally:
    print("Goodbye! ")
