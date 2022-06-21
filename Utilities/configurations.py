import configparser
def getConfig():
    config=configparser.ConfigParser() #configparser method and object creation
    config.read("Utilities/properties.ini") #call read method
    return config