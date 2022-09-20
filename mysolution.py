try:
    number=int(input("please enter a number between 1 and 100:\n"))
    if 1 <= number <= 100:
        if number%3==0:
            print("Fizz")
        elif number%5==0:
            print("Buzz")
        elif number%15==0:
            print("FizzBuzz")
        else:
            print(number)
    else:
        print("The number should be within 1 and 100. Try again")
except:
    print("Please enter a valid integer number between 1 and 100")