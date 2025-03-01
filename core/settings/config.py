from enum import Enum

class Users(Enum):
    USERNAME = "admin"
    PASSWORD = "password123"

class Timeouts(Enum):
    TIMEOUT = 5

class BookingByName(Enum):
    FIRSTNAME = "Sally"
    LASTNAME = "Brown"