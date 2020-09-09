# This is a demo program that generate 6 random numbers, each in the range 0 to 9
# It prints out a 6 digit number which is the concatenation of the random numbers generated

import random

output=""

for i in range(0,6):
    output+=str(random.randint(0,9))

print(output)
