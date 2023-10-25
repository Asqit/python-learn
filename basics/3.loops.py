# Loops
# sometimes, we developers want to do something more than one time
# and rather than hardcoding and repeating the same process over and over again
# we use control-flow structures called loops (while loop, for-loop, for-each loop, do-while...)

# For loop
# this is eqvivalent of a for loop in other languages
for i in range(0, 100):
    print(i)


# While loop
# while loop continues to repeat until it's condition is finally broken
# or unless explicitly specified "break" keyword
i = 0
while True:
    if i == 100:
        break
    i += 1
    print("I am stuck inside a loop")

# Loop controls
# the flow of the loop can be altered by the following keywords
# 1. break      - terminates the loop entirely
# 2. continue   - skips to the next iteration
# 3. pass       - works as a placeholder, basically does nothing
