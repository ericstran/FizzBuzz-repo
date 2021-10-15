# FizzBuzz
# Goal: Count from 1-100 and replace multiples of 3 and 5 with "Fizz" and "Buzz" respectively (including if both are multiples).
# Focus: Make it work.

counter = 1
while counter <= 100:
    if counter % 3 == 0 and counter % 5 == 0:
        print("FizzBuzz")
    elif counter % 3 == 0:
        print("Fizz")
    elif counter % 5 == 0:
        print("Buzz")
    else:
        print(counter)
    counter += 1