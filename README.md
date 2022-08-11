# FizzBuzz
My python solution to the popular FizzBuzz programming excercise

### FizzBuzz
The FizzBuzz problem defined as:
Given an integer (n), returns a string array (1-indexed) where
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Example:
py FizzBuzz.py 15
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

### Alternate FizzBuzz
The same as the normal FizzBuzz problem but the divisors and value outputted when the index is divisible
by the divisor is passed as arguments.

Example:
py AlternateFizzBuzz.py 10 3:Fizz 5:Buzz 10:Jazz
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'BuzzJazz']