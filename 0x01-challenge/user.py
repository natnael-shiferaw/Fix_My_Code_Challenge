#!/usr/bin/python3
"""
User class
"""

class User():
    """ A class representing a user."""

    def __init__(self):
        """ method used for initialization """
        self.__email = None

    @property
    def email(self):
        """ method that returns the email of a user"""
        return self.__email

    @email.setter
    def email(self, value):
        """ method for setting the value of email"""
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value
    
if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)
