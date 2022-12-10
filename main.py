
def prime_checker(number):
    checklist = []
    for divider in range(2,number):
        if number%divider > 0:
            checklist.append(1)
        else: 
            checklist.append(0)

    if all(checklist) == 1:
        print("It's a prime number")
    else:
        print("It's not a prime number")
        
n = int(input("Check this number: "))
prime_checker(number=n)
