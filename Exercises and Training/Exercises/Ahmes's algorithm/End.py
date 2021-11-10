# Is the method where the final stages of the process are performed
def End(result: list[object]):      
    Ending(result[0], result[1])
    return


# Is the method used for writing the result
def Ending(config:  dict, result: list[object]):
    if(config["visible"] and config["save"]):                   # If I have to both write it on the screen and on a file I do a single cycle
        file = open(config["save"][0], config["save"][1])
        for i in result[1]:
            print(i)
            file.write(i)
        print(result[0])
        file.write(result[0])
        file.close()  
    else:
        if(config["visible"]):                                  # If I just have to write it on the screen
            for i in result[1]:                                 # For all lines
                print(i)                                        # I write the line
            print(result[0])                                    # Write the final result
        if(config["save"]):                                     # If I just have to write it to a file
            file = open(config["save"][0], config["save"][1])
            for i in result[1]:                                 # For all lines
                file.write(i)                                   # I write the line
            file.write(result[0])                               # Write the final result
            file.close()                                        #
    return 
