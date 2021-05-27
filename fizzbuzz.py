def fizzbuzz():
    num = 2
    string = "1"
    while num <= 100:
        if num %3  == 0 and num % 5 != 0:
            string+=", Fizz"
        else:
            #print(num)
            string+=", "+str(num)
        num+=1
    return string

