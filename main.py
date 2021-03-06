# 1. use regex - find a valid phone number from a given string
# 2. use regex to find a word that starts with 'Bat' from a given string
# note: use a pipe to separate the options

# 3. find the phone number, where area code is optional.


# 1. use regex - find a valid phone number from a given string
# Import the re module
import re

some_string_with_ph_num = "Hey, call me on 212-555-6363!"

#create a reg ex object to store phone_num_regex variable; use re.compile function
#note: make sure to use raw string by using r in front
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# save the searched string in match_object variable
match_object = phone_num_regex.search(some_string_with_ph_num)

# use group() for actual text from match_object
# print the results
print(match_object.group())
print('=====================================')


# 2. use regex to find a word that starts with 'Bat' from a given string
bat_regex = re.compile(r'Bat(man|mobile|copter)')
match_object = bat_regex.search('Batmobile lost a wheel!')
print(match_object.group())
print('=====================================')



# 3. find the phone number, where area code is optional

# create a regex 
phone_regex = re.compile('(\d\d\d-)?\d\d\d-\d\d\d\d')
match_object_1 = phone_regex.search(some_string_with_ph_num)
match_object_2 = phone_regex.search('Hey, call me on 555-6262!')

print(match_object_1.group())
print(match_object_2.group())