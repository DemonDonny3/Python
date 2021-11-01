from os import path


# define Python user-defined exceptions
class Error(Exception):
    pass


class MyError1(Error):
    pass


class MyError2(Error):
    pass


# Check if the imput have the specific length
def InputChekLength(message: str, check: list[str], length: int):
    while (True):
        try:
            string = input(message)

            for i in check:                                         # Check if the string is already in the lis befaure because it is restrictive case,
                if string == i:                                     # two can have the same length, with this order I can be more efficent
                    raise MyError1

            if len(string) > length:
                raise MyError2
            break

        except MyError1:
            print("This character is already taken, choose another one!")
        except MyError2:
            print("The max number of character is " + length + "!")
            print("You have insert " + len(string) + " character!")
        except:
            print("This is not an acceptable character!")
    return string


# Check the input based on the list given in input
def InputChekList(message: str, check: list[str], error: str):
    while (True):
        try:
            string = input(message).upper()
            for i in string:
                if i not in check:
                    raise
            break
        except:
            if(error != ""):
                print(error + ", you can select only:")
            else:
                print("This caracter is non accptable, you can select only:")
            for l in check:
                print(l)
    return string


# Check input only number
def InputChekNumber(message: str):
    while (True):
        try:
            number = int(input(message))
            break
        except:
            print("That's not a number!")
    return number


# Check if the input is an number
def InputChekNumberList(message: str, check: list[int], error: str):
    while (True):
        try:
            n = int(input(message))
            if n not in check:
                raise MyError1
            break
        except MyError1:
            print(error + ", you can select only:")
            for i in check:
                print(i)
        except:
            print("This is not a number!")
    return n


# Check if the input is an number
def InputCheckPath(message: str):
    while (True):
        try:
            p = input(message)
            if not path.exists(p):
                raise
            break
        except:
            print("The folder location: "+ p + " does not exist, enter a valid path")
    return p


# Check if the input is an number
def InputCheckFile(message: str):
    while (True):
        p = []
        try:
            p.append(input(message))
            for i in p[0]:
                if i < "a" and i > "z":
                    if i < "A" and i > ">":
                        if i < "0" and i > "9":
                            raise MyError1
            p[0] += ".txt"

            start = 1
            if path.exists(p):
                start = InputChekNumberList("In the folder there is already a file with the same name, how you want to proceed:\n" +
                                            "1) Overwrite it;\n" +
                                            "2) Add to the end of the file;\n"+
                                            "3) Change file\n"
                                            [1, 2, 3])

            match start:
                case 1: p.append("w")
                case 2: p.append("a")
                case 3: raise MyError2
            break
        except MyError1:
            print("The file name must not contain special characters or punctuation!")
        except MyError2:
            print("Tell me the file name")
        except:
            print("The folder location: "+ p + " does not exist, enter a valid path!")
    return p
