import time

# Start of UNIX Epoch (seconds since Jan.1.1970)
print(time.ctime(0))

# Current UNIX time in seconds
print(time.time())

# Current time
print(time.ctime(time.time()))  # or just time.ctime()

# Time_Object or Struct_Time
time_obj = time.localtime()  # Local time
# > time_obj = time.gmtime() # UTC Time


# converting time_object to readable human string (month, day, year, h:m:s)
print(time.strftime("%B %d %Y %H:%M:%S", time_obj))


# parsing date string to time_object
time_str = "23 August, 2001"
my_birthday_tobj = time.strptime(time_str, "%d %B, %Y")


# Converts a time_struct into readable string
print(time.asctime(my_birthday_tobj))

# Time since UNIX EPOCH
print(time.mktime(my_birthday_tobj))
