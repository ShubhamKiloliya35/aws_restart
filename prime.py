#given number is prime number or not


number = int(input("enter the number "))
if number > 1:
    for i in range(2, int(number/2)+1):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")
