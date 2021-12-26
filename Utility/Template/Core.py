'''
Name:   Core

Access: public

Description:
    Method used to verify that an input is correct given a list of string of accepted values, 
    with error handling and exceptions

Parameters:
    config      dict            Program's configuration

Returns:
    result      string
'''
# Is the method where the process takes place
def Core(config:  dict) -> str:
    result = Method()               # Is the method used to do the job
    return result


'''
Name:   Method

Access: public

Description:
    Method used to do the job

Parameters:
    config      dict            Program's configuration

Returns:
    result      string
'''
def Method(config:  dict) -> str:
    return