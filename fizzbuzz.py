def fizzbuzz():
    for num in range (1, 100):
        if num %3  == 0 and num % 5 != 0:
            return "Fizz"  
        elif num % 5 == 0 and num % 3 != 0:
            return "Buzz"
        elif num % 3 == 0 and num % 5 == 0:
            return "FizzBuzz"
        else: 
            return num

