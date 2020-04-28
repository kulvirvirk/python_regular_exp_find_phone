# 1. use regex - find a valid phone number from a given string


# Import the re module
import re

some_string_with_ph_num = "Hey, call me on 212-555-6363!"

#create a reg ex object to store phone_num_regex variable; use re.compile function
#note: make sure to use raw string by using r in front
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')