# FizzBuzz
# Goal: Count from 1-100 and replace multiples of 3 and 5 with "Fizz" and "Buzz" respectively (including if both are multiples).
# Focus: Make it more readable

#Difference from initial-attempt:
#   Rather than finding the remainder of counter/3 and counter/5 every time,
#   The multiples of 3 and 5 are kept track of a specific counter that counts to 3 or 5 respectively before resetting to 0.
#   This is done since finding the remainder (division) is much slower than addition/ assignment operations.

#init variables
counter = 0
multThree = 0   #multiple of 3 counter
multFive = 0    #multiple of 5 counter

#loop from 1 to 100 using the "counter" variable
while counter < 100:
    #increment the variables
    multThree += 1
    multFive += 1
    counter += 1

    #variable to print
    string = ""

    #if number is a multiple of 3
    if multThree == 3:
        #add "Fizz" to the print variable
        string += "Fizz"
        #reset the multiple of 3 counter
        multThree = 0
    #if number is multiple of 5
    if multFive == 5:
        #add "Buzz" to the print variable
        string += "Buzz"
        #reset the multiple of 5 counter
        multFive = 0
    #if string is not empty (aka at least one of the prior if statements executed)
    if string != "":
        print(string)
        continue
    #none of the if statements executed, so just print the 1-100 counter.
    print(counter)