# Check input only number
def InputChekNumber(message):
    while (True):
        try:
            number = int(input(message))
            break
        except:
            print("That's not a number!")
    return number


# Main of the program
def Core():
    mylist = []
    start = InputChekNumber("Please enter the starting value:\n")
    end = InputChekNumber("Please enter the ending value:\n")

    if(start % 2 == 1):
        start += 1

    for i in range(start, end, 2):
        mylist.append(i)

    print(mylist)
    return


# Start
Core()
