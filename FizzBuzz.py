# FizzBuzz programming Excercise:
# Description from Leetcode:
# Given an integer (n), returns a string array (1-indexed) where
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

# !/usr/bin/python
import sys


########## Handle Arguments ##########
if (len(sys.argv) != 2):
    print("Please enter one integer argument: FizzBuzz.py [n]")
    exit()

try:
    n = int(sys.argv[1]);
except:
    print("Please enter one integer argument: FizzBuzz.py [n]")
    exit()


######## Create output array ########
out = []
for i in range(1, (n + 1)):
    value = ""
    if (i % 3 == 0):
        value += "Fizz"
    if (i % 5 == 0):
        value += "Buzz"
    if (value == ""):
        value = str(i)
    out.append(value)


print(out)
    