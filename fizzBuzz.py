# FizzBuzz
# Goal: Count from 1-100 and replace multiples of 3 and 5 with "Fizz" and "Buzz" respectively (including if both are multiples).
# Focus: Make it more efficient

counter = 0
multThree = 0
multFive = 0
while counter < 100:
    multThree += 1
    multFive += 1
    counter += 1
    string = ""
    if multThree == 3:
        string += "Fizz"
        multThree = 0
    if multFive == 5:
        string += "Buzz"
        multFive = 0
    if string != "":
        print(string)
        continue
    print(counter)