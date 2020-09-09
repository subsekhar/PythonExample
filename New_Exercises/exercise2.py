# This program generates a 6 digit random number 
# It combines 6 randomly generated numbers each in the range 0 to 9

import random

output = ""
for i in range(0,6):
    output+=str(random.randint(0,9))

print("The winning lottery ticket is:", output)
