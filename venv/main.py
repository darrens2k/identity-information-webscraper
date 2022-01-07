# Tester File

# import necessary modules
from searches import instagramSearch, linkedinSearch
from target import Target
import time

# define sample inputs for target person
name = "Darren Singh"
location = "Toronto"
occupation = "Student"
school = "York University"
attributes = "YorkU, YU, Astrophysics, Computer Science"

# create instance of target class
darren = Target(name, occupation, location, school, attributes)

# create second test instance
lauren = Target("Lauren Nazareth", "Student", "Toronto", "Wilfred Laurier University", "wlu, math, finance, markham")

# test call to instargramSearch() Function
# instagramSearch("tester77707", "tester789", lauren, sleep=5, iterations=3)

# test print
# print(lauren.getInstagramResults())

# testing linkedinSearch function
linkedinSearch("testerduster8@gmail.com", "tester789", lauren)

