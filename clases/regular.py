import re

# line = "my age is 222 and my hight is 173 and I"
# line2 = "i am from 222 and bla bla "
# my_age =  re.search(r'my\sage\sis\s(\d+)',line)
# m = re.search(r'(\d+).*\s(\d+).*',line)
# y = re.findall(r'(\d+)',line)
# z = re.search(r'(\d+)',line)
#


line  = "27:11:2004"
line2  = "27-11-2004"
def get_date(line):
    m = re.search(r'(\d+)[:-](\d+)[:-](\d+)',line)
    day = m.group(1)
    month = m.group(2)
    year = m.group(3)
    print(f" day = {day} month={month} year ={year}")


get_date(line)
get_date(line2)
# if m:
# 	print(f"matched string is {m.group(1)} in index ({m.start(1)},{m.end(1)})")
# else:
#  	print ("No match!!")
#
# re.search(r'(age).*(\w{5}).*\s(\d+).*',line).group(3)
#
# match = re.search(r'b\w+', 'foobar')
# str = 'purple alice-b@google.com monkey dishwasher'
# match = re.search(r'\w+@\w+', str)
# match1 = re.search(r'[\w.-]+@[\w.-]+', str)
# match2 = re.search(r'([\w.-]+)@([\w.-]+)', str)
#
# print("match",match)
#
# phons = "1234567890  456-166-7890 789-456-7890 +1 098-456-7890"
# code = re.findall(r"(?:(\+1)[ -]?)?(\d{3})[ -]?(\d{3})[ -]?(\d{4})",phons) #(\d{3})[ -]?(\d{3})[ -]?(d{3})
# print("code",code)