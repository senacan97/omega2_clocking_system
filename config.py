"""Configuration file for Clocking System"""

#Python Modules
from enum import Enum

class Config(Enum):
    #USER SETTINGS
    DELAY_SECONDS = 30 #DELAY FOR CLOCKING AGAIN IN SECONDS (AVOID DUPLICATE)
    OLED_EXPANSION = 0 #1 = ON OR 0 = OFF (USE OLED EXPANSION)
    ID_STOP_SYSTEM = "b5c6e7bb" #Card id to stop the system

    #DONT CHANGE
    OK_IMG = "img/image_ok.lcd" #Path for OK img
    ERROR_IMG = "img/image_error.lcd" #Path for error img

    #MYSQL CONFIGURATION
    HOST = "192.168.1.233"
    PORT = "3307"
    USER = "omega"
    PASSWD = "0m3g4n3d*"
    DATABASE = "staff"
