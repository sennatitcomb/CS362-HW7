def fizzbuzz():
    num = 2
    string = "1"
    while num <= 100:
        if num %3  == 0 and num % 5 != 0:
            string+=", Fizz"
        elif num % 5 == 0 and num % 3 != 0:
            string+= ", Buzz"
        elif num % 3 == 0 and num % 5 == 0:
            string+= ", FizzBuzz"
        else:
            #print(num)
            string+=", "+str(num)
        num+=1
    return string

