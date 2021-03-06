'''
Name:   End

Access: public

Description:
    Method used to ending the process are performed

Parameters:
    result      list[object]    Result of the process and the config

Returns:

'''
def End(result: list[object]):      
    Ending(result[0], result[1])                                    # Use the AskEnd config for output the process and data from the Core
    return


'''
Name:   Ending

Access: public

Description:
    Method used for writing the result

Parameters:
    config      dictionary      Program's configuration
    result      list[object]    The final result

Returns:

'''
def Ending(config:  dict, result: list[object]):
    if(config["visible"] and config["save"]):                       # If I have to both write it on the screen and on a file I do a single cycle
        file = open(config["save"][0], config["save"][1])           # Open the file select in the start config
        for i in result:                                            # For all lines

            print(i)                                                # Write the line on the terminal
            file.write(i)                                           # Write the line on the file

        print("\n\n")                                               # Separate one iteration from the other
        file.write("\n\n")                                          # Separate one iteration from the other

        file.close()                                                # Close the file
    else:
        if(config["visible"]):                                      # If I just have to write it on the screen
            for i in result:
                print(i)
        print("\n\n")                                               # Separate one iteration from the other
        
        if(config["save"]):                                         # If I just have to write it to a file
            file = open(config["save"][0], config["save"][1])
            for i in result:
                file.write(i)
            file.write("\n\n")                                      # Separate one iteration from the other
            file.close()
    return 
