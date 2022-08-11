# Alternate FizzBuzz programming Excercise:
# Description from Leetcode:
# Given an integer (n), list of divisors, and list of corresponding values returns a string array 
# (1-indexed) where when the index is divisible by the divisor, the output element contains the 
# corresponding value.
# Format: AlternateFizzBuzz.py [n] [divisor:value] [divisor:value]
# Example: py AlternateFizzBuzz.py 10 3:Fizz 5:Buzz 10:Jazz
# ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "BuzzJazz"]

import sys

divisors = []
fizzBuzzMap = {}

######## Handle Arguments ########
try: 
    n = int(sys.argv[1])
    
    for i in range(2, len(sys.argv)):
        arg = sys.argv[i]
        keyValuePair = arg.split(":")

        if (len(keyValuePair) != 2):
            print("invalid divisor value pair")
            exit()
        
        divisor = int(keyValuePair[0])
        value = keyValuePair[1]
        divisors.append(divisor)
        fizzBuzzMap[divisor] = value
except:
    print ("Please use the format AlternateFizzBuzz.py [n] [divisor:value] [divisor:value] ...")
    exit()


######## Create output array ########
out = []
for i in range(1, (n + 1)):
    value = ""
    for divisor in divisors:
        if (i % divisor == 0):
            value += fizzBuzzMap[divisor]
    
    if (value == ""):
        value = str(i)
    
    out.append(value)

print(out)
